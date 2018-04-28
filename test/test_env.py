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
        dfs = Dfs.create("test_dfs.yml")
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
        op = Env.create("test_envdemo.yml")
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
        print('op.model.dc_list', getattr(op.model, "dc_list", "<dc> Not Found"))
        # print(
        #     'op.model.url.input[0].timeseries', getattr(op.model.url.input[0], "timeseries", "<timeseries> Not Found"))
        # print('op.model.url.input[1].cate_seasonal.isBook',
        #       getattr(op.model.url.input[1].cate_seasonal, "isBook", "<isBook> Not Found"))
        # print('op.model.url.input[2].calendar.b', getattr(op.model.url.input[2].calendar[0], "b", "<b> Not Found"))
        # print('op.model.url.input[2].calendar.e', getattr(op.model.url.input[2].calendar[1], "e", "<e> Not Found"))
        # print('op.model.url.input[3].promotion', getattr(op.model.url.input[3], "promotion", "<promotion> Not Found"))
        # print('op.model.url.output.dir', getattr(op.model.url.output, "dir", "<dir> Not Found"))
        # print('op.model.url.output.file', getattr(op.model.url.output, "file", "<file> Not Found"))

    # def test_metaSelf(self):
    #     print('---------------------------------------')
    #     print('|    Biz Info')
    #     print('---------------------------------------')
    #     op = Biz.create("test_env.yml")
    #     print('     ---------------------------------------')
    #     print('     |    MetaSelf Result Info')
    #     print('     ---------------------------------------')
    #     print('op.meta', op.meta)
    #     print('op.metaSelf', op.metaSelf)
    #     print('op.dfs.metaSelf', op.dfs.metaSelf)
    #     print('op.env.url.metaSelf', op.env.url.metaSelf)
    #
    #     print('op.env.url.input[0].metaSelf', op.env.url.input[0].metaSelf)
    #     print('op.env.url.input[1].metaSelf', op.env.url.input[1].metaSelf)
    #     print('op.env.url.input[1].seasonal.metaSelf', op.env.url.input[1].seasonal.metaSelf)
    #     print('op.env.url.input[2].metaSelf', op.env.url.input[2].metaSelf)
    #     print('op.env.url.input[3].metaSelf', op.env.url.input[3].metaSelf)
    #     print('op.env.url.input[4].metaSelf', op.env.url.input[4].metaSelf)

    # def test_biz_option(self):
    #     print('---------------------------------------')
    #     print('|    Biz Info')
    #     print('---------------------------------------')
    #     op = Biz.create("test_env.yml")
    #     op.parseExpr()
    #     print('     ---------------------------------------')
    #     print('     |    Option Result Info')
    #     print('     ---------------------------------------')
    #     print('createSparkSubmit', op.createSparkSubmit())
    # print('op.metaSelf', op.metaSelf)
    # print('op.dfs.metaSelf', op.dfs.metaSelf)
    # print('op.env.url.metaSelf', op.env.url.metaSelf)
    #
    # print('op.env.url.input[0].metaSelf', op.env.url.input[0].metaSelf)
    # print('op.env.url.input[1].metaSelf', op.env.url.input[1].metaSelf)
    # print('op.env.url.input[1].seasonal.metaSelf', op.env.url.input[1].seasonal.metaSelf)
    # print('op.env.url.input[2].metaSelf', op.env.url.input[2].metaSelf)
    # print('op.env.url.input[3].metaSelf', op.env.url.input[3].metaSelf)
    # print('op.env.url.input[4].metaSelf', op.env.url.input[4].metaSelf)


if __name__ == '__main__':
    unittest.main()
