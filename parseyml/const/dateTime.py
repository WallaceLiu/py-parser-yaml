# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:

日期常量

"""

from parseyml.utils.dateTime import yesterday, tomorrow, today, toStr

TODAY = toStr(today())

TODAY_YEAR = today().year

YESTERDAY = toStr(yesterday())

TOMORROW = toStr(tomorrow())
