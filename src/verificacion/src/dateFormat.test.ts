
import CsvUtil from './util/CsvUtil';
import TestSuite from './util/TestSuite';

TestSuite.runForTag('ISO', file => CsvUtil.checkColumnDateFormat(file, 'yyyy-MM-dd'));
