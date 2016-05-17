'''
Created on 11May,2016

@author: linyufeng
'''
import unittest
from model.Asset import Asset
from AssetService import AssetService


class AssetServiceTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInsert(self):
        service = AssetService()
        assets = []
        startTime, endTime, directory = "2016511 07:15", "2016511 07:20", "/home/pi/slides"
        fileName, fileType, duration, sequence = "Ads.mp4", "video", 225, 1
        asset = Asset(startTime, endTime, directory, fileName, fileType, duration,sequence)
        assets.append(asset)
        service.insertAssets(assets)
        assert True
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'AssetServiceTest.testInsert']
    unittest.main()