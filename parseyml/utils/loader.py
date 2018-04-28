# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:

"""
import yaml
import sys
import os
from parseyml.base.base import Base

if sys.version.startswith('2'):
    import ConfigParser
else:
    import configparser


class LoaderUtils(Base):
    def __init__(self):
        pass

    @staticmethod
    def decodeYml(filePath):
        f = open(filePath)
        return yaml.load(f)

    @staticmethod
    def ini(confPath):
        """
        加载ini文件
        兼容 py2 py3
        :param confPath: ini文件路径
        :return:
        """
        if not os.path.isfile(confPath):
            raise IOError(confPath, '<{f}> Not Found in {c}'.format(f=confPath, c=LoaderUtils.__class__.__name__))

        config = None

        if sys.version.startswith('2'):
            config = ConfigParser.ConfigParser()
        else:
            config = configparser.ConfigParser()

        config.read(confPath)

        return config
