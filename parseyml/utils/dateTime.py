# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:
"""

from datetime import datetime, timedelta
import datetime as dt
import time


def timestamp2Datetime(value, format='%Y-%m-%d %H:%M:%S'):
    """
    时间戳转换成日期
    :return:
    :param value: int       时间戳
    :param format: string   日期格式，例如：%Y-%m-%d %H:%M:%S
    :return:
    """
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def datetime2Timestamp(dt, f='%Y-%m-%d %H:%M:%S'):
    """
    日期字符串转换成时间戳
    :param dt: datetime or string  日期
    :param format: string       日期格式，默认为%Y-%m-%d %H:%M:%S
    :return:
    """
    if isinstance(dt, str):
        return time.mktime(time.strptime(dt, f))
    else:
        return time.mktime(dt.timetuple())


def format(dt, f='%Y-%m-%d'):
    """
    字符串格式化日期
    :param dt: 日期类型       日期
    :param format: string   日期格式，默认为%Y-%m-%d %H:%M:%S
    :return:
    """
    return datetime.strptime(dt, f)


def toStr(dt, format='%Y-%m-%d'):
    # type: (object, object) -> object
    """
    日期转换成字符串
    :param dt: datetime     日期
    :param format: string   日期格式，默认为%Y-%m-%d %H:%M:%S
    :return:
    """
    return dt.strftime(format)


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


def addStr(dt, d):
    """

    :param dtStr:
    :param d:
    :return:
    """
    return add(format(dt), d)


def addStrToStr(dt, day):
    return toStr(addStr(dt, day))


def addBySec(ts, s):
    """
    按秒增加日期
    :param ts: 日期
    :param s: 秒
    :return:
    """
    dt = time.localtime(ts)
    d = datetime(dt.tm_year, dt.tm_mon, dt.tm_mday, dt.tm_hour, dt.tm_min,
                 dt.tm_sec)
    aSec = timedelta(seconds=s)
    now = d + aSec
    return time.mktime(now.timetuple())


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


def sub(d1, d2):
    """
    日期相减
    :param d1: 日期1
    :param d2: 日期2
    :return:
    """
    return d2 - d1


def subStr(d1, d2, f='%Y-%m-%d %H:%M:%S'):
    """
    日期相减
    :param d1: 字符串，日期1
    :param d2: 字符串，日期2
    :param f: 日期格式
    :return: 整型，小时
    """
    return sub(format(d1, f), format(d2, f))


def getDays(start_date, end_date, f='%Y-%m-%d'):
    """
    根据起始时间和结束时间创建日期数组
    :param start_date: 字符串，开始日期
    :param end_date: 字符串，结束时间
    :param f: 日期格式
    :return: 数组 [-,-,-,-,-,-,...]
    """
    s_dt = format(start_date, f)
    e_dt = format(end_date, f)
    return [toStr(add(s_dt, i), f) for i in range((e_dt - s_dt).days + 1)]


def getDaysByDay(date, d, dir=1, f='%Y-%m-%d'):
    """
    根据起始时间和天数创建日期数组
    :param date: 字符串，开始日期
    :param d: 天数
    :param f: 日期格式
    :return: 数组 [-,-,-,-,-,-,...]
    """
    s_dt = format(date, f)
    return [toStr(add(s_dt, dir * i), f) for i in range(d)]
