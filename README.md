# screenly-tools-schedulespreadsheet

=========================

An introduction to import schedule spreadsheet data into Screenly's table assets 



xlrd setup in linux
------------

1. download xlrd from this  https://pypi.python.org/pypi/xlrd
2. install the xlrd
gunzip -c xlrd.targ.gz | tar xf - # unpacks into directory xlrd
cd xlrd
python setup.py install

copy the vidoes and images into associated folder under Screenly os
-------------------------
for example:
/home/pi/videos for videos
/home/pi/slides for images


the format of schedule spread sheet
-----------------------------

1. only the first sheet data will be imported into database
2. the format of the spread sheet must be set as follow:
------------------------------------

2.1 the first row is the name of the fields:

StartTime   EndTime Directory   FileName    FileType    Duration    Sequence

2.2 the rest row is the value of the fields:
the format of the cell must be text;
the StartTime and EndTime must be writen in this format: 
date+space+hours(in 24 hours style)+":"+minutes such as 2016511 07:15
the fileName must with suffix: such as Ads.mp4
below is a spreadsheet example:

StartTime       EndTime          Directory        FileName        FileType    Duration    Sequence
2016511 07:15   2016511 07:20    /home/pi/videos  Ads.mp4         video       225          1
2016511 07:15   2016511 07:20    /home/pi/slides  pur.jpg         image       10           2





