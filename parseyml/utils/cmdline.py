# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:
"""


class CmdLineUtils:
    """
    命令行

    格式，二维数组:
    [["命令行1", "说明", "--命令行 备注", 是否必选, 默认值],[...],...]
    例如:
    [["dim", "维度", "--dim  维度，包括销量，成交价格等，必填", True, 'sales'],...]
    """

    @staticmethod
    def initialize(argv, optional):
        """
        初始化参数

        :argv: 命令行sys.argv
        :optional：自定义的命令行选项，二维数组
        :return: 字典
        """
        try:
            p = {}
            for i in range(len(argv)):
                if argv[i][:2] == "--":
                    p[argv[i][2:]] = argv[i + 1]
            for dp in optional:
                if dp[0] not in p.keys():
                    if dp[3] is False:
                        p[dp[0]] = dp[4]
                    elif dp[3] is True:
                        print("ERROR: 缺少必要的参数，" + dp[2])
                        return False
            return p
        except:
            print("参数格式错误")
            return False
