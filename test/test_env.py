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
        dfs = Dfs.create("test_deom_simple.yml")
        print('---------------------------------------')
        print('|    Env Meta Info')
        print('---------------------------------------')
        print('dfs.raw', dfs.raw)
        print('dfs.rawFile', dfs.rawFile)
        print('---------------------------------------')
        print('|    Env Properties Info')
        print('---------------------------------------')
        print('dfs.metaSelf', dfs.metaSelf)
        print('---------------------------------------')
        print('|    Env Properties Info')
        print('---------------------------------------')
        print('dfs.debug', dfs.debug)
        print('dfs.name_node', dfs.name_node)
        print('dfs.data_mart', dfs.data_mart)
        print('dfs.base', dfs.base)
        print('dfs.dfs', dfs.dfs)
        print('dfs.schema', dfs.schema)

    def test_biz_property(self):
        env = Env.create("test_demo_complex.yml")
        print('---------------------------------------')
        print('|    Env Meta Info')
        print('---------------------------------------')
        print('dfs.raw', env.raw)
        print('dfs.rawFile', env.rawFile)
        print('---------------------------------------')
        print('|    property Info')
        print('---------------------------------------')
        print('env.debug', getattr(env, "debug", "<debug> Not Found"))
        print('---------------------------------------------------')
        print('env.name', getattr(env, "name", "<name> Not Found"))
        print('---------------------------------------------------')
        print('env.cmd.loc', getattr(env.cmd, "loc", "<loc> Not Found"))
        print('env.cmd.option', getattr(env.cmd, "option", "<option> Not Found"))
        print('---------------------------------------------------')
        print('env.task.name', getattr(env.task, "name", "<name> Not Found"))
        print('env.task.spark.shell', getattr(env.task.spark, "shell", "<shell> Not Found"))
        print('env.task.hive', getattr(env.task, "hive", "<hive> Not Found"))
        print('---------------------------------------------------')
        print('env.dfs.name_node', getattr(env.dfs, "name_node", "<name_node> Not Found"))
        print('env.dfs.data_mart', getattr(env.dfs, "data_mart", "<data_mart> Not Found"))
        print('env.dfs.base', getattr(env.dfs, "base", "<base> Not Found"))
        print('env.dfs.dfs', getattr(env.dfs, "dfs", "<dfs> Not Found"))
        print('env.dfs.schema', getattr(env.dfs, "schema", "<schema> Not Found"))
        print('---------------------------------------------------')
        print('env.model.url.input[0].timeseries',
              getattr(env.model.url.input[0], "timeseries", "<timeseries> Not Found"))
        print('env.model.url.output.dir', getattr(env.model.url.output, "dir", "<dir> Not Found"))
        print('env.model.url.output.file', getattr(env.model.url.output, "file", "<file> Not Found"))


if __name__ == '__main__':
    unittest.main()
