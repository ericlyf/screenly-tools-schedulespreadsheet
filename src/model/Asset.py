'''
Created on 11May,2016

@author: linyufeng
'''
from utils.TimeZoneConverter import TimeZoneConverter

class Asset(object):
    '''
    contain the values will be insert into table Asset
    '''

    convert = TimeZoneConverter();
    
    def __init__(self, startTime, endTime, directory, fileName, fileType, duration, sequence):
        self.startTime = self.convert.victoriaToUCT(startTime)
        self.endTime = self.convert.victoriaToUCT(endTime)
        self.directory = directory
        self.fileName = fileName
        self.fileType = fileType
        self.duration = int(duration)
        self.sequence = int(sequence)
        
    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
    def getDirectory(self):
        return self.directory
    
    def getFileName(self):
        return self.fileName
    
    def getFileType(self):
        return self.fileType
    
    def getDuration(self):
        return self.duration
    
    def getSequence(self):
        return self.sequence
    
    def __eq__(self,other):
        if isinstance(other, self.__class__):
            if self.startTime == other.startTime:
                if self.endTime == other.endTime:
                    if self.directory == other.directory:
                        if self.duration == other.duration:
                            if self.fileName == other.fileName:
                                if self.fileType == other.fileType:
                                    return True
        return False
                            
        
