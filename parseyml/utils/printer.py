# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:

"""

import sys


class PrintUtils:
    """
    输出工具类

    """

    @staticmethod
    def tuple(*str):
        """

        :param str:
        :return:
        """
        for s in str:
            print(s)

    @staticmethod
    def dictionary(**kv):
        """
        按key顺序输出dict
        兼容 py2 py3
        :param kv:
        :return:
        """
        s = sorted(kv.iteritems(), key=lambda d: d[0]) \
            if sys.version.startswith('2') else \
            sorted(kv.items(), key=lambda d: d[0])

        for i in s:
            print('{0}={1}'.format(i[0], i[1]))
