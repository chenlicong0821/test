# -*- coding: utf-8 -*-

import os


def findAllFile(topPath):
    fileList = []

    for root, dirs, files in os.walk(topPath):
        for fileName in files:
            fileList.append(os.path.join(root, fileName))

    return fileList


topPath = '/home/chenlicong/code/me/test'
fileList = findAllFile(topPath)
for f in fileList:
    print f
