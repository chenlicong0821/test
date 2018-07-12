#!/usr/bin/python
#-*- coding: utf-8 -*-

import datetime
import pytz

print repr(pytz.timezone('Asia/Shanghai'))
print repr(pytz.timezone('Asia/Chongqing'))

tz = pytz.timezone('Asia/Shanghai')

dtNow = datetime.datetime.now(tz)
print repr(dtNow)
dtThis = datetime.datetime(2018, 7, 12, 17, 0, 0, tzinfo=tz)
print repr(dtThis)
print (dtNow-dtThis).total_seconds()

dtNow2 = datetime.datetime.now()
print repr(dtNow2)
dtNow2 = tz.localize(dtNow2)
print repr(dtNow2)
dtThis2 = datetime.datetime(2018, 7, 12, 17, 0, 0)
print repr(dtThis2)
dtThis2 = tz.localize(dtThis2)
print repr(dtThis2)
print (dtNow2-dtThis2).total_seconds()
