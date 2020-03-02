#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
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


class TCQtIdx(IntEnum):
    MARKET_ID = 0               # 市场标识，1-sh，51-sz
    CHS_NAME = 1                # 证券中文简称
    RAW_SYMBOL = 2              # 证券代码（不含市场标识）
    LAST_PRICE = 3              # 最新价格
    PREV_CLOSE = 4              # 昨收价
    OPEN_PRICE = 5              # 今开价
    TOTAL_VOLUME = 6            # 总成交量：手，实际同VOLUME
    OUT_BUY = 7                 # 外盘：手
    IN_SELL = 8                 # 内盘：手
    BUY1_PRICE = 9              # 买1价
    BUY1_VOLUME = 10            # 买1量：手
    BUY2_PRICE = 11             # 买2价
    BUY2_VOLUME = 12            # 买2量
    BUY3_PRICE = 13             # 买3价
    BUY3_VOLUME = 14            # 买3量
    BUY4_PRICE = 15             # 买4价
    BUY4_VOLUME = 16            # 买4量
    BUY5_PRICE = 17             # 买5价
    BUY5_VOLUME = 18            # 买5量
    SELL1_PRICE = 19            # 卖1价
    SELL1_VOLUME = 20           # 卖1量：手
    SELL2_PRICE = 21            # 卖2价
    SELL2_VOLUME = 22           # 卖2量
    SELL3_PRICE = 23            # 卖3价
    SELL3_VOLUME = 24           # 卖3量
    SELL4_PRICE = 25            # 卖4价
    SELL4_VOLUME = 26           # 卖4量
    SELL5_PRICE = 27            # 卖5价
    SELL5_VOLUME = 28           # 卖5量
    CURRENT_VOLUME = 29         # 当前成交量
    QUOTE_DATETIME = 30         # 行情日期时间
    NET_CHG = 31                # 涨跌额
    PCT_CHG = 32                # 涨跌幅（%）
    HIGH_PRICE = 33             # 最高价格
    LOW_PRICE = 34              # 最低价格
    LAST_VOLUME_AMOUNT = 35     # 最新价/成交量(手)/成交额(元)
    VOLUME = 36                 # 成交量(手)
    AMOUNT = 37                 # 成交额(万元)，整数
    TURNOVER_RATE = 38          # 换手率（%）
    PE_TTM = 39                 # 市盈率(TTM)
    SECU_STATUS = 40            # 股票状态,允许有多个状态，每种状态一个字符表示: 无或空表示正常, D 退市, S 停牌, U 未上市
    TODAY_HIGH_PRICE = 41       # 当天最高价格
    TODAY_LOW_PRICE = 42        # 当天最低价格
    AMPLITUDE = 43              # 当天振幅（%）
    CIRC_MARKET_VALUE = 44      # 流通市值(亿)
    TOTAL_MARKET_VALUE = 45     # 总市值(亿)
    PB = 46                     # 市净率
    HIGH_LIMIT = 47             # 涨停价
    LOW_LIMIT = 48              # 跌停价
    QUANT_RELATIVE = 49         # 量比
    WEI_CHA = 50                # 委差(手)
    AVG_PRICE = 51              # 均价
    PE_DYNAMIC = 52             # 市盈率(动)
    PE_STATIC = 53              # 市盈率(静)
    IDX54 = 54
    IDX55 = 55
    BETA_VALUE = 56             # 贝塔值
    AMOUNT2 = 57                # 成交额(万元)，带小数
    POST_AMOUNT = 58            # 盘后交易额(万元)
    POST_VOLUME = 59            # 盘后交易量(股)
    IDX60 = 60
    SECU_TYPE = 61              # 证券类别，GP-A-KCB表示股票-A股-科创板，ZS表示指数
    IDX62 = 62
    IDX63 = 63
    DPS = 64                    # 股息率(%)
    IDX65 = 65
    IDX66 = 66


class dataFromTencent():
    def __init__(self):
        self.STARMarketPattern = re.compile(r'sh68[89]+')
        self.marketIdDict = {'1':'sh', '51':'sz'}

    def _getVolume(self, code, rawVolume):
        if (self.STARMarketPattern.match(code)):    # 科创板
            return rawVolume
        else:                                       # 非科创板
            return rawVolume * 100

    def _checkCodeFlag(self, codeFlag, code):
        if codeFlag.startswith('v_') and (codeFlag[2:] == code):
            return True
        else:
            log.warning('codeFlag:{} not match code:{}'.format(codeFlag, code))
            return False

    def _checkCodeData(self, codeData, code):
        if self.marketIdDict[codeData[TCQtIdx.MARKET_ID]] + codeData[TCQtIdx.RAW_SYMBOL] == code:
            return True
        else:
            log.warning('codeFlag:{} not match code:{}'.format(codeFlag, code))
            return False

    def _parseData(self, text, codeList):
        qtList = text.split(';\n')[:-1]     # 每一条数据都是以';\n'结尾，split之后最后一项就是空字符串、所以忽略之
        for i, qt in enumerate(qtList):
            codeFlag, codeData = qt.split('=')
            info = codeData.strip('"').split('~')
            log.debug(codeData)

            # idx = 0
            # for item in info:
            #     print(idx, item, TCQtIdx._value2member_map_[idx])
            #     idx += 1

            code = codeList[i]
            if not(self._checkCodeFlag(codeFlag, code) and self._checkCodeData(info, code)):
                continue

            volume = self._getVolume(code, int(info[TCQtIdx.VOLUME] or 0))
            quoteTime = info[TCQtIdx.QUOTE_DATETIME]
            quoteTime = datetime.datetime.strptime(quoteTime, "%Y%m%d%H%M%S")
            if quoteTime < datetime.datetime(2020, 1, 1):
                log.warning("quoteTime {} incorrect".format(quoteTime))
                continue
            pe = float(info[TCQtIdx.PE_TTM]) if info[TCQtIdx.PE_TTM] else 0.0
            cap = float(info[TCQtIdx.TOTAL_MARKET_VALUE]) if info[TCQtIdx.TOTAL_MARKET_VALUE] else 0.0
            print(volume, quoteTime, pe, cap)
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
