# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author:

"""


def isScalars(v):
    """
    if or not scalars date type
    :param self:
    :param v:
    :return:
    """
    if isinstance(v, int):
        return True
    elif isinstance(v, float):
        return True
    elif isinstance(v, bool):
        return True
    elif isinstance(v, complex):
        return True
    elif isinstance(v, str):
        return True
    elif isinstance(v, list):
        print(1)
        for l in v:
            if isinstance(l, dict):
                return False
        print(1)
        return True
    else:
        return False


# def isScalarsList(v):
#     """
#     if or not scalars date type
#     :param self:
#     :param v:
#     :return:
#     """
#     if isinstance(v, list):
#         for l in v:
#             if isinstance(l, dict):
#                 return False
#
#         return True
#     else:
#         return False


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
