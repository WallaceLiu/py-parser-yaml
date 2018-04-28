# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning11@jd.com

通用配置文件
"""
import unittest
from parseyml.env.dfs import Dfs
from parseyml.env.env import Env


class TestEnv(unittest.TestCase):

    def test_dfs(self):
        print('---------------------------------------')
        print('|    Dfs Info')
        print('---------------------------------------')
        dfs = Dfs.create("test_deom_simple.yml")
        print('     ---------------------------------------')
        print('     |    Result Info')
        print('     ---------------------------------------')
        print('dfs.debug', dfs.debug)
        print('dfs.raw', dfs.raw)
        print('dfs.rawFile', dfs.rawFile)
        print('dfs.metaSelf', dfs.metaSelf)
        print('dfs.name_node', dfs.name_node)
        print('dfs.data_mart', dfs.data_mart)
        print('dfs.base', dfs.base)
        print('dfs.dfs', dfs.dfs)
        print('dfs.hive', dfs.hive)

    def test_biz_property(self):
        print('---------------------------------------')
        print('|    Biz Meta Info')
        print('---------------------------------------')
        op = Env.create("test_demo_complex.yml")
        print('     ---------------------------------------')
        print('     |    property Result Info')
        print('     ---------------------------------------')
        print('op.debug', getattr(op, "debug", "<debug> Not Found"))
        print('---------------------------------------------------')
        print('op.name', getattr(op, "name", "<name> Not Found"))
        print('---------------------------------------------------')
        print('op.cmd.loc', getattr(op.cmd, "loc", "<loc> Not Found"))
        print('op.cmd.option', getattr(op.cmd, "option", "<option> Not Found"))
        print('---------------------------------------------------')
        print('op.task.name', getattr(op.task, "name", "<name> Not Found"))
        print('op.task.spark', getattr(op.task, "spark", "<spark> Not Found"))
        print('op.task.hive', getattr(op.task, "hive", "<hive> Not Found"))
        print('---------------------------------------------------')
        print('op.cmd.loc', getattr(op.cmd, "loc", "<loc> Not Found"))
        print('op.cmd.option', getattr(op.cmd, "option", "<option> Not Found"))
        print('---------------------------------------------------')
        print('op.dfs.name_node', getattr(op.dfs, "name_node", "<name_node> Not Found"))
        print('op.dfs.data_mart', getattr(op.dfs, "data_mart", "<data_mart> Not Found"))
        print('op.dfs.base', getattr(op.dfs, "base", "<base> Not Found"))
        print('op.dfs.dfs', getattr(op.dfs, "dfs", "<dfs> Not Found"))
        print('op.dfs.hive', getattr(op.dfs, "hive", "<hive> Not Found"))
        print('---------------------------------------------------')


if __name__ == '__main__':
    unittest.main()
