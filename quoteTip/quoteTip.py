#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import os
import requests
import time
# import re

def logInit(logfile):
    logdir = os.path.dirname(logfile)
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s || %(filename)s:%(lineno)d || %(levelname)s || %(name)s || %(message)s',
                        datefmt='%a %Y/%m/%d %H:%M:%S',
                        filename=logfile,
                        filemode='a')

def fetchFromTencent(codeList):
    for i in range(3):
        try:
            time.sleep(1)
            req = requests.get("http://qt.gtimg.cn/q={}".format(','.join(codeList)), timeout=2)
            if 200 != req.status_code:
                log.warning('req is not success:{}, {}'.format(req.status_code, req.text))
                continue

            # print(req.headers['Content-Type'])
            # match = re.search('charset=(\S+)', req.headers['Content-Type'])
            # if match:
            #     encoding = match.group(1)
            #     print(encoding)
            # text = req.content.decode(req.encoding)
            text = req.text
            qtList = text.split(';\n')
            for qt in qtList[:-1]:
                codeFlag, codeData = qt.split('=')
                codeData = codeData.strip('"')
                info = codeData.split('~')
                print(info)
            break
        except Exception as e:
            log.exception('fetch is error: {}'.format(e))

if __name__ == '__main__':
    logInit('./log/quoteTip.log')
    log = logging.getLogger(__name__)

    codeList = ['sh000919', 'sh000001', 'sh000922']
    fetchFromTencent(codeList)
