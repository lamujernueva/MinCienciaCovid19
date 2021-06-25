
import * as fs from 'fs';

import parse from 'csv-parse/lib/sync';
import { DateTime } from 'luxon';

const PARSE_OPTIONS = {
	columns: true,
	skip_empty_lines: false
};
const PARSE_OPTIONS_SKIP = {
	columns: true,
	skip_empty_lines: true
};

export default class CsvUtil
{
	public static checkColumnDateFormat(file: string, format: string): void
	{
		test(`${file} should have columns with date format ${format}`, () =>
		{
			const contents = fs.readFileSync(file);
			const records = parse(contents, PARSE_OPTIONS_SKIP) as any[];
			expect(records.length).toBeGreaterThan(0);
			const record = records[0];
			const properties = Object.keys(record);
			const hasValidDates = properties
				.map(p => DateTime.fromFormat(p, format))
				.some(d => d.isValid);
			expect(hasValidDates).toBe(true);
		});
	}

	public static checkNoEmptyLines(file: string): void
	{
		test(`${file} should not have empty lines`, () =>
		{
			const contents = fs.readFileSync(file);
			const result = parse(contents, PARSE_OPTIONS) as any[];
			expect(result).not.toBe(null);
		});
	}
}
