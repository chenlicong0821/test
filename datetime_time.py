#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import datetime
import time

#-------------------------------------------------
# conversions to strings
#-------------------------------------------------
# datetime object to string
dt_obj = datetime(2008, 11, 10, 17, 53, 59)
date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
print date_str

# time tuple to string
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print date_str

#-------------------------------------------------
# conversions to datetime objects
#-------------------------------------------------
# time tuple to datetime object
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
dt_obj = datetime(*time_tuple[0:6])
print repr(dt_obj)

# date string to datetime object
date_str = "2008-11-10 17:53:59"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print repr(dt_obj)

# timestamp to datetime object in local time
timestamp = 1226527167.595983
dt_obj = datetime.fromtimestamp(timestamp)
print repr(dt_obj)

# timestamp to datetime object in UTC
timestamp = 1226527167.595983
dt_obj = datetime.utcfromtimestamp(timestamp)
print repr(dt_obj)

#-------------------------------------------------
# conversions to time tuples
#-------------------------------------------------
# datetime object to time tuple
dt_obj = datetime(2008, 11, 10, 17, 53, 59)
time_tuple = dt_obj.timetuple()
print repr(time_tuple)

# string to time tuple
date_str = "2008-11-10 17:53:59"
time_tuple = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print repr(time_tuple)

# timestamp to time tuple in UTC
timestamp = 1226527167.595983
time_tuple = time.gmtime(timestamp)
print repr(time_tuple)

# timestamp to time tuple in local time
timestamp = 1226527167.595983
time_tuple = time.localtime(timestamp)
print repr(time_tuple)

#-------------------------------------------------
# conversions to timestamps
#-------------------------------------------------
# time tuple in local time to timestamp
time_tuple = (2008, 11, 13, 5, 59, 27, 2, 317, 0)
timestamp = time.mktime(time_tuple)
print repr(timestamp)

#-------------------------------------------------
# results
#-------------------------------------------------
# 2008-11-10 17:53:59
# 2008-11-12 13:51:18
# datetime.datetime(2008, 11, 12, 13, 51, 18)
# datetime.datetime(2008, 11, 10, 17, 53, 59)
# datetime.datetime(2008, 11, 13, 5, 59, 27, 595983)
# datetime.datetime(2008, 11, 12, 21, 59, 27, 595983)
# time.struct_time(tm_year=2008, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=0, tm_yday=315, tm_isdst=-1)
# time.struct_time(tm_year=2008, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=0, tm_yday=315, tm_isdst=-1)
# time.struct_time(tm_year=2008, tm_mon=11, tm_mday=12, tm_hour=21, tm_min=59, tm_sec=27, tm_wday=2, tm_yday=317, tm_isdst=0)
# time.struct_time(tm_year=2008, tm_mon=11, tm_mday=13, tm_hour=5, tm_min=59, tm_sec=27, tm_wday=3, tm_yday=318, tm_isdst=0)
# 1226527167.0
