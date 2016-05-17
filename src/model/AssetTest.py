'''
Created on 11May,2016

@author: linyufeng
'''
import unittest
from Asset import Asset
from utils.TimeZoneConverter import TimeZoneConverter

class AssetTest(unittest.TestCase):
    
  
    def testConstructor(self):
        startTime, endTime, directory = "2016511 07:15", "2016511 07:20", "/home/pi/slides"
        fileName, fileType, duration, sequence = "Ads.mp4", "video", 225, 1
        asset = Asset(startTime, endTime, directory, fileName, fileType, duration, 1.0)
        checkStartTime = "20160510 21:15" == asset.getStartTime().strftime(TimeZoneConverter.dateFormat)
        checkEndTime = "20160510 21:20" == asset.getEndTime().strftime(TimeZoneConverter.dateFormat)
        checkDirectory = directory == asset.getDirectory()
        checkFileName = fileName == asset.getFileName()
        checkFileType = fileType == asset.getFileType()
        checkDuration = duration == asset.getDuration()
        checkSequence = sequence == asset.getSequence()
        
        self.assertTrue(checkStartTime and checkEndTime and checkDirectory and checkFileName and checkFileType and checkDuration and checkSequence, "should be equal")
        
    def testEqual(self):
        assetOne = Asset("2016511 07:15","2016511 07:15",3,4,5,6,7)
        assetTwo = Asset("2016511 07:15","2016511 07:15",3,4,5,6,7)
        
        self.assertTrue(assetOne == assetTwo, "compare two asset object")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'AssetTest.testConstructor','AssetTest.testEqual']
    unittest.main()
