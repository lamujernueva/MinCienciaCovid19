
import CsvUtil from './util/CsvUtil';
import TestSuite from './util/TestSuite';

TestSuite.runForAll(file => CsvUtil.checkNoEmptyLines(file));
