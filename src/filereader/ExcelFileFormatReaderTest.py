'''
Created on 11May,2016

@author: linyufeng
'''
import unittest
from filereader.ExcelFileFormatReader import ExcelFileFormatReader
from model.Asset import Asset


class ExcelFileFormatReaderTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCanHandler(self):
        filePath = "bigScreenScheduleTest.xlsx"
        reader = ExcelFileFormatReader()
        self.assertTrue(reader.canHandler(filePath), "check if the file can be path")
        
    def testRead(self):
        filePath = "bigScreenScheduleTest.xlsx"
        reader = ExcelFileFormatReader()
        rows = reader.read(filePath)
        startTime = "2016511 07:15"
        endTime = "2016511 07:20"
        fileName = "Ads.mp4"
        fileType = "video"
        duration = "225.0"
        sequence = "1.0"
        
        
        for row in rows:
            if startTime != row[reader.startTime]:
                raise ValueError("startTime is not correct")
            if endTime !=row[reader.endTime]:
                raise ValueError("endTime is not correct")
            if fileName != row[reader.fineName]:
                raise ValueError("fileName is not correct")
            if fileType != row[reader.fileType]:
                raise ValueError("fileType is not correct")
            if duration != row[reader.duration]:
                raise ValueError("duration is not correct")
            if sequence != row[reader.sequence]:
                raise ValueError("sequence is not correct")
             
        assert True
        
    def testGetAssets(self):
        filePath = "bigScreenScheduleTest.xlsx"
        reader = ExcelFileFormatReader()
        reader.read(filePath)
        startTime, endTime, directory = "2016511 07:15", "2016511 07:20", "/home/pi/videos"
        fileName, fileType, duration, sequence = "Ads.mp4", "video", 225, 1.0
        expAsset = Asset(startTime, endTime, directory, fileName, fileType, duration, sequence)
        
        assets = reader.getAssets()
        for asset in assets:
            if (expAsset == asset):
                assert True
            else:
                assert False
            
        
                
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'filereader.ExcelFileFormatReaderTest.testCanHandler','filereader.ExcelFileFormatReaderTest.testRead','ExcelFileFormatReaderTest.testGetAssets']
    unittest.main()