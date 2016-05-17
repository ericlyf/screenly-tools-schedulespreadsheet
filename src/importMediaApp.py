#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Created on 11May,2016

@author: linyufeng
'''
from filereader.ExcelFileFormatReader import ExcelFileFormatReader
from tableservice.AssetService import AssetService
import sys
import os.path

if len (sys.argv) != 2 :
    print "Usage: importMediaApp.py <excel file>"
    sys.exit (1)
filePath = sys.argv[1]
if not os.path.isfile(sys.argv[1]):
    print "the file is not exist: %s" % filePath
    
reader = ExcelFileFormatReader()
reader.read(filePath)
assets = reader.getAssets()
service = AssetService()
service.insertAssets(assets)

