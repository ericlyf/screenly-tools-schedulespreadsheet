'''
Created on 10May,2016

@author: linyufeng
'''
from datetime import datetime, timedelta
import pytz

class TimeZoneConverter():
    """ use to convert different time zone to uct
    current only support austrialia/Victoria to uct
    """
    victorialTimeZone = "Australia/Victoria"
    dateFormat = "%Y%m%d %H:%M"
    
    def victoriaToUCT(self, dateStr):
        date = datetime.strptime(dateStr, self.dateFormat) 
#         local = pytz.timezone(self.victorialTimeZone)
#         local_dt = local.localize(date, is_dst=None)
#         uct_dt = local_dt.astimezone(pytz.utc)
        uct_dt = date - timedelta(hours = 10)
        return uct_dt
    
    
    
