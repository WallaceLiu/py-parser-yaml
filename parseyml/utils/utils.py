# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""
import yaml
from datetime import datetime, timedelta
import datetime as dt
import time


def decodeYml(filePath):
    f = open(filePath)
    return yaml.load(f)


def add(dt, d):
    """
    按天增加日期
    :param dt: datetime     日期
    :param d: int           天
    :return:
    """
    aDay = timedelta(days=d)
    now = dt + aDay
    return now


def yesterday():
    """
    昨天
    :return:
    """
    now = datetime.now()
    return add(now, -1)


def today():
    """
    昨天
    :return:
    """
    return datetime.now()


def tomorrow():
    """
    明天
    """
    now = datetime.now()
    return add(now, 1)


def nowWeekth():
    return time.strftime("%W")


def weekth(y, m, d):
    return dt.date(y, m, d).isocalendar()


def isMixedList(v):
    """
    if or not mixed list
    :param v:
    :return:
    """
    number_c = 0
    dict_c = 0
    str_c = 0
    list_c = 0
    c = len(v)
    if isinstance(v, list):
        i = 0
        while i < c:
            if isinstance(v[i], dict):
                dict_c += 1
            if isinstance(v[i], int) or isinstance([i], float):
                number_c += 1
            if isinstance(v[i], str):
                str_c += 1
            if isinstance(v[i], list):
                list_c += 1
            i += 1

        # print(number_c, dict_c, str_c, list_c)
        return (number_c == c, str_c == c, dict_c == c, dict_c > 0 and dict_c < c)
    else:
        return (False, False, False, False)


def distinct(arr):
    """
    数组去重
    :param arr:
    :return:
    """
    return list(set(arr))
