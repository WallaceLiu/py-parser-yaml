# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:
"""

from datetime import datetime, timedelta
import datetime as dt
import time


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
