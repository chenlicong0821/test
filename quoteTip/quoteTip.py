#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import os
import requests
import re
import time
from enum import IntEnum

def logInit(logfile):
    logdir = os.path.dirname(logfile)
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s || %(levelname)s || %(name)s || %(filename)s:%(lineno)d || %(message)s',
                        datefmt='%a %Y/%m/%d %H:%M:%S',
                        filename=logfile,
                        filemode='a')


class txQtIdx(IntEnum):
    MARKET_ID = 0          # 市场标识，1-sh，51-sz
    CHS_NAME = 1                  # 证券中文简称
    RAW_SYMBOL = 2                  # 证券代码（不含市场标识）
    LAST_PRICE = 3                 # 最新价格
    PREV_CLOSE = 4           # 昨收价
    OPEN_PRICE = 5                 # 今开价
    TOTAL_VOLUME = 6       # 总成交：手
    OUT_BUY = 7              # 外盘：手
    IN_SELL = 8               # 内盘：手
    BUY1_PRICE = 9                 # 买1价
    BUY1_VOLUME = 10              # 买1量
    BUY2_PRICE = 11                 # 买2价
    BUY2_VOLUME = 12                # 买2量
    BUY3_PRICE = 13                # 买3价
    BUY3_VOLUME = 14               # 买3量
    BUY4_PRICE = 15                 # 买4价
    BUY4_VOLUME = 16                # 买4量
    BUY5_PRICE = 17                 # 买5价
    BUY5_VOLUME = 18                # 买5量
    SELL1_PRICE = 19                # 卖1价
    SELL1_VOLUME = 20               # 卖1量
    SELL2_PRICE = 21                # 卖2价
    SELL2_VOLUME = 22               # 卖2量
    SELL3_PRICE = 23                # 卖3价
    SELL3_VOLUME = 24               # 卖3量
    SELL4_PRICE = 25                # 卖4价
    SELL4_VOLUME = 26               # 卖4量
    SELL5_PRICE = 27                # 卖5价
    SELL5_VOLUME = 28               # 卖5量
    CURRENT_VOLUME = 29             # 当前成交量
    QUOTE_DATETIME = 30              # 行情日期时间
    NET_CHG = 31                    # 涨跌额
    PCT_CHG = 32                    # 涨跌幅（%）
    HIGH_PRICE = 33                 # 最高价格
    LOW_PRICE = 34                  # 最低价格
    VOLUME = 35                     # 成交数量 （单位1）
    AMOUNT = 36                     # 成交金额
    TURNOVER_RATE = 37              # 换手率（%）
    PE = 38                  # 市盈率
    SECU_STATUS = 39                # 股票状态,允许有多个状态，每种状态一个字符表示: 无或空表示正常, D 退市, S 停牌, U 未上市
    TODAY_HIGH_PRICE = 40           # 当天最高价格
    TODAY_LOW_PRICE = 41            # 当天最低价格
    AMPLITUDE = 42                  # 当天振幅（%）
    CIRC_MARKET_VALUE = 43   # 流通市值
    TOTAL_MARKET_VALUE = 44    # 总市值（亿）
    ENG_NAME = 45               # 英文名称
    EPS = 46         # 每股收益
    WEEK52_HIGH = 47             # 52周最高
    WEEK52_LOW = 48              # 52周最低
    PRICE_CHG = 49                   # 价格变动
    IDX50 = 50
    IDX51 = 51
    IDX52 = 52
    IDX53 = 53
    IDX54 = 54
    IDX55 = 55
    IDX56 = 56
    IDX57 = 57
    IDX58 = 58
    IDX59 = 59
    IDX60 = 60
    IDX61 = 61
    IDX62 = 62
    IDX63 = 63
    IDX64 = 64
    IDX65 = 65
    IDX66 = 66


class dataFromTencent():
    def __init__(self):
        self.STARMarketPattern = re.compile(r'sh68[89]+')

    def _getVolume(self, code, rawVolume):
        if (self.STARMarketPattern.match(code)):    # 科创板
            return rawVolume
        else:                                       # 非科创板
            return rawVolume * 100

    def _parseData(self, text, codeList):
        qtList = text.split(';\n')
        for qt in qtList[:-1]:
            codeFlag, codeData = qt.split('=')
            codeData = codeData.strip('"')
            info = codeData.split('~')
            log.info(info)

            idx = 0
            for item in info:
                print(idx, item, txQtIdx._value2member_map_[idx])
                idx += 1

            # volume = self._getVolume(code, float(info[36] or 0))
            # quoteTime = info[30]
            # quoteTime = datetime.datetime.strptime(quoteTime, "%Y%m%d%H%M%S")
            # if quoteTime < datetime.datetime(2000, 1, 1):
            #     return (None, "quoteTime %s incorrect" % quoteTime)
            # pe = info[39] if len(info) > 39 else 0.0
            # cap = info[45] if len(info) > 45 else 0.0
            # parsedData = {'source_name': self.source, 'code': code, 'name': info[1], 'last': info[3], 'close': info[4],
            #               'open': info[5], 'amountchange': info[31], 'percentchange': info[32],
            #               'high': info[33], 'low': info[34], 'volume': volume, 'turnover': info[37], 'pe': pe,
            #               'cap': cap, 'week52high': 0, 'week52low': 0,
            #               'quoteTime': quoteTime}
            #
            # if parsedData['pe'] == '':
            #     parsedData['pe'] = 0.00
            # parsedData['cap'] = float(parsedData['cap'] or 0) * 100000000
            # parsedData['turnover'] = float(parsedData['turnover'] or 0) * 10000
            # try:
            #     eps = float(parsedData['last']) / float(parsedData['pe'])
            #     parsedData['eps'] = round(eps, 4)
            # except:
            #     parsedData['eps'] = 0
            # try:
            #     share = float(parsedData['cap']) / float(parsedData['last'])
            #     parsedData['share'] = round(share, 4)
            # except:
            #     parsedData['share'] = 0
            # return (parsedData, 'OK')

    def fetchData(self, codeList):
        for i in range(3):
            try:
                time.sleep(1)
                req = requests.get("http://qt.gtimg.cn/q={}".format(','.join(codeList)), timeout=2)
                if 200 != req.status_code:
                    log.warning('request is not success:{}, {}'.format(req.status_code, req.text))
                    continue

                # print(req.headers['Content-Type'])
                # match = re.search('charset=(\S+)', req.headers['Content-Type'])
                # if match:
                #     encoding = match.group(1)
                #     print(encoding)
                # text = req.content.decode(req.encoding)
                text = req.text
                self._parseData(text, codeList)
                break
            except Exception as e:
                log.exception('fetch failed: {}'.format(e))


if __name__ == '__main__':
    logInit('./log/quoteTip.log')
    logname = os.path.splitext(os.path.basename(__file__))[0]
    log = logging.getLogger(logname)

    # codeList = ['sh000919', 'sh000001', 'sh000922']
    codeList = ['sh688001', 'sz000063', 'sh000001']
    txData = dataFromTencent()
    txData.fetchData(codeList)
