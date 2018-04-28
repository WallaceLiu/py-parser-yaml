# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:

"""
import glob


class IOUtils:
    def __init__(self):
        pass

    @staticmethod
    def readAll(filePath):
        data = None
        with open(filePath, 'r') as f:
            data = f.read()

        return data

    @staticmethod
    def getFiles(dir):
        """
        获得指定目录下的文件
        :param dir: 目录路径，可以写文件通配符
        :return:
        """
        return glob.glob(dir)
