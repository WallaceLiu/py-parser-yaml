# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""
from parseyml.utils.utils import *
from parseyml.genv.base import BaseEnv, base
import parseyml.const.dateTime as CONST_DT
from parseyml.genv.const import *
import inspect


class Env(BaseEnv):

    def __init__(self, raw, rawFile):
        BaseEnv.__init__(self)

        self.raw = raw
        self.rawFile = rawFile
        self.__meta = []

        self.__init()

    def __init(self):
        if self.__isValid():
            self.parseFile(self.raw)
            self.setConst()
            self.parseExpression(None)

    def parseExpr(self):
        option = self.getAttrValueByDot(SETION_CMD_OPTION)
        self.parseExpression(option)

    @staticmethod
    def create(ymlFile):
        """
        创建biz示例
        :param ymlFile: yml配置文件
        :param option: 命令行选项
        :return:
        """
        d = decodeYml(ymlFile)

        o = Env(d, ymlFile)

        return o

    def __isValid(self):
        """
        验证yml文件
        :return:
        """
        try:
            debug = self.raw["debug"]
            return True
        except:
            raise KeyError("Error: Key <debug> Not Exist in {f}, Occured in {cls}.{fn}.". \
                           format(cls=self.clsName, fn=inspect.stack()[0][3], f=self.rawFile))

    def createSparkSubmit(self):
        spark = self.getAttrValueByDot(SETION_TASK_SPARK)
        params = []
        params.append(SPARK_CMD)

        if spark is not None:
            for k in spark:
                for v in k:
                    params.append(v)

        loc = self.getAttrValueByDot(SETION_CMD_LOC)
        params.append(loc)

        option = self.getAttrValueByDot(SETION_CMD_OPTION)

        if option is not None:
            for opt in option:
                for a, b, c, d, v in opt:
                    params.append("--" + a)
                    params.append(v)

        return params

    def initCmdLineOption(self, argv):
        """
        初始化参数

        param = cmdline.init_params(sys.argv, p)
        date = param["date"]

        :param argv: 通过环境变量传入的参数 例如：["--date",'2016-04-18',"--name","zhangsan"]
                     例如： [["date",  "输入数据的产生日期","--date    输入数据的产生日期，选填，默认是今天，格式为yyyy-mm-dd", False, '2014-04-22']]
        :return: 参数
        """
        try:
            p = {}
            for i in range(len(argv)):
                if argv[i][:2] == "--":
                    p[argv[i][2:]] = argv[i + 1]

            for dp in self.getAttrValueByDot(SETION_CMD_OPTION):
                if dp[0] not in p.keys():
                    if dp[3] is False:
                        p[dp[0]] = dp[4]
                        dp[4] = p[dp[0]]
                    elif dp[3] is True:
                        raise KeyError("ERROR: Miss requir parameters <{p}> in {f}, Ocurred in {c}.{fn}.". \
                                       format(p=dp[2], f=self.rawFile, c=self.clsName, fn=inspect.stack()[0][3]))
            return p
        except:
            raise KeyError("ERROR: parameter format Of {f}, Occured in {c}.{fn}.". \
                           format(c=self.clsName, fn=inspect.stack()[0][3], f=self.fnName))

    def setConst(self):
        o = base()
        o.setAttr("TODAY", CONST_DT.TODAY)
        o.setAttr("TODAY_YEAR", CONST_DT.TODAY_YEAR)
        o.setAttr("YESTERDAY", CONST_DT.YESTERDAY)
        o.setAttr("TOMORROW", CONST_DT.TOMORROW)

        self.setAttr("const", o)
