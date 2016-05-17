'''
Created on 11May,2016

@author: linyufeng
'''
from model.Asset import Asset
from xlrd import open_workbook
import string


class ExcelFileFormatReader(object):
    '''
    classdocs
    '''
    suffix = ["xlsx" , "xls"]
    startTime, endTime, directory, fineName, fileType, duration, sequence = "StartTime", "EndTime", \
    "Directory", "FileName", "FileType", "Duration", "Sequence"

   
    def canHandler(self, filePath):
        filePieces = string.split(filePath, ".")
        suffixIndex = len(filePieces) - 1
        fileSuffix = filePieces[suffixIndex]
        return fileSuffix in self.suffix
        
    def read(self, filePath):
        workBook = open_workbook(filePath)
        satSheet = workBook.sheet_by_index(0)
        
        #read header values into the list
        keys = [satSheet.cell(0,col_index).value for col_index in xrange(satSheet.ncols)]
        
        dict_list = []
        
        for row_index in xrange(1, satSheet.nrows):
            d = {keys[col_index]: str(satSheet.cell(row_index, col_index).value) for col_index in xrange(satSheet.ncols)}
            dict_list.append(d);
        
        self.dict_list = dict_list
        return dict_list
    
    def getAssets(self):
        assets = []
        for d in self.dict_list:
            startTime = d[self.startTime]
            endTime = d[self.endTime]
            directory = d[self.directory]
            fileName = d[self.fineName]
            fileType = d[self.fileType]
            duration = d[self.duration]
            duration = float(duration)
            sequence = d[self.sequence]
            sequence = float(sequence)
            asset = Asset(startTime, endTime, directory, fileName, fileType, duration, sequence)
            assets.append(asset)
            
        return assets;
            
            
            
            
            
                        