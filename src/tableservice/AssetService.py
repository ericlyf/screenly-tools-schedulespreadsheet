'''
Created on 11May,2016

@author: linyufeng
'''
import uuid
import os.path
import sqlite3
from contextlib import contextmanager

class AssetService(object):
 
    def __init__(self):
        '''
        Constructor
        '''
        self.__dbFile = "screenly.db"
        self.conn = sqlite3.connect(self.__dbFile, detect_types=sqlite3.PARSE_DECLTYPES)
        
        
    def insertAssets(self, assets):
        with self.cursor(self.conn) as c:
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='assets'")
            if c.fetchone() is None:
                c.execute('CREATE TABLE assets(' + \
                            'asset_id text primary key, name text, uri text, md5 text, ' + \
                            'start_date timestamp, end_date timestamp, duration text, ' + \
                            'mimetype text, is_enabled integer default 0, ' + \
                            'nocache integer default 0, play_order integer default 0)')
                
        # This takes a key value pair structure and converts it into a SQL insertAssets statement
        comma = ','.join
        create = lambda keys: 'insert into assets (' + comma(keys) + ') values (' + comma(['?'] * len(keys)) + ')'
        
        for assetObj in assets:
            imagePath = os.path.join(assetObj.getDirectory(), assetObj.getFileName())
            if not os.path.isfile(imagePath):
                print('%s does not exist' % imagePath)
                continue
            # Generate asset hash
            assetHash = uuid.uuid4().hex
            
            # Generate entry in database
            asset = {
                     'asset_id': assetHash,
                     'name': assetObj.getFileName(),
                     'uri': imagePath,
                     'start_date': assetObj.getStartTime(),
                     'play_order': assetObj.getSequence(),
                     'end_date': assetObj.getEndTime(),
                     'duration': assetObj.getDuration(),
                     'mimetype': assetObj.getFileType(),
                     'is_enabled': 1
                     }
            with self.commit(self.conn) as c:
                c.execute(create(asset.keys()), asset.values())

            # TODO: make this optional
            print "Imported: %s --> %s" % (assetObj.getFileName(), assetHash)
        
        
    
    # This function copied from screenly-ose/db.py
    @contextmanager
    def cursor(self, connection):
        cur = connection.cursor()
        yield cur
        cur.close()

    # This function copied from screenly-ose/db.py
    @contextmanager
    def commit(self, connection):
        cur = connection.cursor()
        yield cur
        connection.commit()
        cur.close()
        
