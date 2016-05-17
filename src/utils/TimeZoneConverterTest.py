'''
Created on 11May,2016

@author: linyufeng
'''
import unittest
from TimeZoneConverter import TimeZoneConverter

class TimeZoneConverterTest(unittest.TestCase):

    def testVictoriaToUCT(self):
        dateStr = "2016511 07:15"
        convert = TimeZoneConverter();
        resultUct = convert.victoriaToUCT(dateStr)
        resultUctStr = resultUct.strftime(TimeZoneConverter.dateFormat)
        expUctStr = "20160510 21:15"
        self.assertTrue(expUctStr == resultUctStr, "string date equal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TimeZoneConverterTest.testVictoriaToUCT']
    unittest.main()