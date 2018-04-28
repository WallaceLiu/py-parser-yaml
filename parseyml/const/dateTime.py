# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""
from parseyml.utils.utils import yesterday, tomorrow, today

format = '%Y-%m-%d'

TODAY = today().strftime(format)

TODAY_YEAR = today().year

YESTERDAY = yesterday().strftime(format)

TOMORROW = tomorrow().strftime(format)
