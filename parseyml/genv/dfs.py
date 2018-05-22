# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""

from parseyml.utils.utils import decodeYml
from parseyml.genv.base import BaseEnv
import inspect


class Dfs(BaseEnv):
    """

    For Example:

    base    ['hdfs://ns15/user']
    dfs     ['hdfs://ns15/user/cmo_ipc']
    hive    ['hdfs://ns15/user/cmo_ipc/<?e>.db']

    """

    def __init__(self, raw, rawFile, nameNode=None):
        BaseEnv.__init__(self)

        self.raw = raw
        self.rawFile = rawFile

        self.name_node = None
        self.data_mart = None
        self.base = None
        self.dfs = None
        self.hive = None

        self.__init(nameNode)

    @staticmethod
    def create(ymlFile, nameNode=None):
        d = decodeYml(ymlFile)
        o = Dfs(d, ymlFile, nameNode)

        return o

    def __init(self, nameNode):
        if self.raw is None:
            raise RuntimeError("Error: Property <raw> is None, Occured in {cls}.{fn}.". \
                               format(cls=self.clsName, fn=inspect.stack()[0][3]))
        print('Parse File...')
        if self.__isValid():
            self.parseFile(self.raw)

            if nameNode is not None:
                self.name_node = nameNode

            print('Parse Expression...')
            self.parseExpression(None)

    def __isValid(self):
        try:
            debug = self.raw["debug"]
            name_node = self.raw["name_node"]
            data_mart = self.raw["data_mart"]
            base = self.raw["base"]
            dfs = self.raw["dfs"]
            hive = self.raw["schema"]
            return True
        except:
            raise KeyError(
                    "Error: Key <debug>,<name_node>,<data_mart>,<base>,<dfs>,<hive> Not Exist in {f}, Occured in {cls}.{fn}.". \
                        format(cls=self.clsName, fn=inspect.stack()[0][3], f=self.rawFile))
