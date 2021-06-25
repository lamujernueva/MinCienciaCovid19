
import FileUtil from './FileUtil';

type FileRunner = (file: string) => void;

export default class TestSuite
{
	public static runForTag(tag: string, runner: FileRunner): void
	{
		const files = FileUtil.getFilesByTag(tag);
		if (!files)
			throw new Error(`No files found for tag: ${tag}`);
		files.forEach(file => runner(file));
	}

	public static runForAll(runner: FileRunner): void
	{
		FileUtil
			.getAllFiles()
			.forEach(file => runner(file));
	}
}
