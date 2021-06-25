
import * as fs from 'fs';
import * as path from 'path';

import * as Enumerable from 'linq';
import wildcard from 'wildcard-match';

import Files from '../config/Files';

type FilesByTag = { [key: string]: string[] };

const CSV_EXTENSION = '.csv';
const BASE_DIR = path.join(__dirname, '../../../../output');

class FileUtil
{
	private allFiles: string[];
	private filesByTag: FilesByTag;

	public constructor()
	{
		this.allFiles = Array.from(FileUtil.generateAllCsvFiles());
		this.filesByTag = this.generateFilesByTag();
		this.checkAllFilesHaveAMatch();
	}

	public getAllFiles(): string[]
	{
		return this.allFiles;
	}

	public getFilesByTag(tag: string): string[]
	{
		return this.filesByTag[tag];
	}

	private checkAllFilesHaveAMatch(): void
	{
		const patterns = Object
			.keys(Files)
			.map(p => path.join(BASE_DIR, p))
			.map(p => wildcard(p));
		this.allFiles.forEach(file =>
		{
			if (!patterns.some(p => p(file)))
				throw new Error(`No patterns found for: ${file}`);
		});
	}

	private generateFilesByTag(): FilesByTag
	{
		const keys = Object.keys(Files);
		return Enumerable
			.from(keys)
			.select(key => Files[key])
			.selectMany(tags => Enumerable.from(tags))
			.distinct()
			.select(tag => {
				const tagMatchers = keys
					.filter(key => Files[key].includes(tag))
					.map(p => path.join(BASE_DIR, p))
					.map(p => wildcard(p));
				const files = this.allFiles
					.filter(file => tagMatchers.some(matcher => matcher(file)));
				return { tag, files };
			})
			.toObject(
				x => x.tag,
				x => x.files) as FilesByTag;
	}

	private static *generateAllCsvFiles(dir: string = BASE_DIR): Generator<string>
	{
		const entries = fs.readdirSync(dir, { withFileTypes: true });
		for (const entry of entries)
		{
			const res = path.resolve(dir, entry.name);
			if (entry.isDirectory())
				yield* FileUtil.generateAllCsvFiles(res);
			else if (res.endsWith(CSV_EXTENSION))
				yield res;
		}
	}
}

export default new FileUtil();

