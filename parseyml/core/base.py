# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""
import re
from parseyml.base.base import ReflectBase
import copy as cp
from parseyml.utils.utils import isMixedList, distinct


class base(ReflectBase): pass


# """
# 切换开发和上线环境<?e>
# :param s:
# :param debug:
# :return:
# """
switchEenv = lambda s, debug: str(s).replace('<?e>', 'dev' if debug else 'app')

switchPenv = lambda s, v: str(s).replace('<?p>', v)


class BaseEnv(ReflectBase):
    __express = '{[\w\.]+}'
    __primaryList = '0x\d+'
    __META_PROPERTY = "metaSelf"

    def __init__(self):
        ReflectBase.__init__(self)
        self.debug = True

    # ------------------------------------------
    #
    # 解析文件
    #
    # ------------------------------------------
    def parseFile(self, o):
        """
        解析文件
        :param o: 根对象，所有对象都会挂在它的下面
        :return:
        """

        def _setAttribute(o, attr, v):
            """
            设置属性
            :param o: 对象
            :param attr: 属性
            :param v: 值
            :return: 
            """
            o.setAttr(attr, v)
            o.meta = attr
            o.metaSelf = attr

        def _isSetAttribute(v):
            """
            是否设置属性
            :param v: 值
            1）dict不设置
            2）纯数字不设置
            3）其他情况需要设置
            :return:
            """
            if isinstance(v, dict):
                return False
            elif isinstance(v, list):
                (scalarNumber, scalarStr, scalarDict, mixedDict) = isMixedList(v)
                isScalarsList = \
                    (scalarNumber, scalarStr, scalarDict, mixedDict) == (True, False, False, False) or \
                    (scalarNumber, scalarStr, scalarDict, mixedDict) == (False, True, False, False)

                return True if isScalarsList else False
            else:
                return True

        def _parseList(parent, attr, v):
            """
            解析list
            :param parent: 父对象
            :param attr: 属性
            :param v: 值
            :return:
            """
            # print(' -RR,PL,')
            t = []
            for l in v:
                if isinstance(l, dict):
                    # print('     -RRR,PL, V={v}'.format(v=l))
                    po = base()
                    po.metaSelf = l.keys()
                    po.meta = l.keys()
                    _parse(po, l)
                    t.append(po)
                else:
                    t.append(l)

            _setAttribute(parent, attr, t)

        def _parseDict(parent, attr, v):
            """
            解析dict
            :param parent:
            :param attr:
            :param v:
            :return:
            """
            # print(' -PD,  P={p},V={v}'.format(p=id(parent), v=v))

            po = base()
            _parse(po, v)
            _setAttribute(parent, attr, po)

        def _parse(parent, o):
            """
            解析
            :param parent: parent object
            :param o: object value
            :return:
            """
            for attr in o.keys():
                v = o[attr]
                isDone = _isSetAttribute(v)

                # print('R,   P={p},IS={d},A={a},V={v}'.format(p=id(parent), d=isDone, a=attr, v=v))

                if isDone:
                    _setAttribute(parent, attr, v)
                else:
                    if isinstance(v, list):
                        _parseList(parent, attr, v)
                    elif isinstance(v, dict):
                        _parseDict(parent, attr, v)
                    else:
                        raise RuntimeError('Error: Parse Unknow.')

        # main
        print('Parse File...')

        for attr in o.keys():
            v = o[attr]
            isDone = _isSetAttribute(v)

            # print('M,   P={p},IS={d},A={a},V={v}'.format(p=id(self), d=isDone, a=attr, v=v))

            if isDone:
                _setAttribute(self, attr, v)
            else:
                if isinstance(v, list):
                    _parseList(self, attr, v)
                elif isinstance(v, dict):
                    _parseDict(self, attr, v)
                else:
                    raise RuntimeError('Error: Parse Unknow.')

    # ------------------------------------------
    #
    # 解析表达式
    #
    # ------------------------------------------

    def parseExpression(self, option):
        """
        保证替换所有表达式
        :param option: 外部参数
        :return:
        """

        print('Parse Expression...')

        self._isStopParse = True
        self._isStop = False

        self.__parseExpression(self.debug, option)
        self._isStop = self._isStopParse

        while not self._isStop:
            self._isStopParse = True
            self.__parseExpression(self.debug, option)
            self._isStop = self._isStopParse

        self._isStopParse = True
        self._isStop = False

    def __parseExpression(self, debug, option):
        """
        解析表达式
        :param option: 外部参数
        :return:
        """

        def _isStopParse(val):
            vars = _findExpress(val)

            if vars is not None:
                for v in vars:
                    t = v.replace("{", "").replace("}", "").split('.')
                    if len(t) > 1:
                        return False
                return True
            else:
                return False

        def _findExpress(val):
            v = re.findall(self.__express, str(val), re.S | re.I)
            return distinct(v)

        def _compute(p, attr, value):

            def _canCompute(v):
                """
                if or not can compute expression
                :param v:
                :return:
                """

                if isinstance(v, int):
                    return None
                elif isinstance(v, float):
                    return None
                elif isinstance(v, bool):
                    return None
                elif isinstance(v, str):
                    vars = _findExpress(v)
                    return vars if len(vars) > 0 else None
                elif isinstance(v, list):
                    vars = _findExpress(str(v))
                    return vars if len(vars) > 0 else None
                else:
                    return None

            def _replaceExpr(o, vars, option):
                t = str(cp.deepcopy(o))
                for v in vars:
                    attr = v.replace("{", "").replace("}", "")

                    attrVal = self.getAttrValueByDot(attr)
                    # print(" **_replaceExpr attrVal {v}".format(v=attrVal))
                    if option is not None and attr in option.keys():
                        attrVal = option[attr]

                    if attrVal is not None:
                        t = t.replace(v, str(attrVal))

                return t

            vars = _canCompute(value)
            # print(" **canCompute {v}".format(v=vars))
            if vars is not None:
                v = _replaceExpr(value, vars, option)
                # print(" **replaceExpr {v}".format(v=v))
                if v is not None:
                    # print(" **setAttr A={a},V={v}".format(a=attr, v=v))

                    self._isStopParse = self._isStopParse and _isStopParse(v)

                    v = switchEenv(v, debug)

                    p.setAttr(attr, eval(v) if isinstance(value, list) else v)

        def _isPrimary(v):

            v = re.findall(self.__primaryList, str(v), re.S | re.I)
            return True if len(v) <= 0 else False

        def _traverseLst(o, attr, v):
            """
            recursion list
            :param o:
            :param attr:
            :param v:
            :return:
            """

            def _list(o, attr, v):
                """
                :param o:
                :param attr:
                :param v:
                :return:
                """
                print("_traverseList,A={a}".format(a=attr))

                isPrimary = _isPrimary(v)

                if isPrimary:
                    print("*DONE A={a}".format(a=attr))
                    _compute(o, attr, v)
                else:
                    for l in v:
                        print('         RL,A={a}'.format(a=l.metaSelf))
                        _traverse(l)  # must be dict

            # main
            print("_traverseLst,A={a}".format(a=attr))
            if isinstance(v, list):
                _list(o, attr, v)
            else:
                # print("*DONE A={a},V={v}".format(a=attr, v=v))
                _compute(o, attr, v)

        def _traverse(o):
            """
            parse
            :param o: object value
            :return:
            """
            for attr in o.metaSelf:
                v = self.getAttrObj(attr, o)

                print(' R,A={a}'.format(a=attr))

                if hasattr(v, self.__META_PROPERTY):
                    isOver = len(v.metaSelf) <= 0

                    print(' R,ISDONE={d},A={a}'.format(d=isOver, a=attr))

                    if isOver:
                        _traverseLst(o, attr, v)
                    else:
                        _traverse(v)
                else:
                    _traverseLst(o, attr, v)

        # main
        for attr in self.metaSelf:
            v = self.getAttrObj(attr, self)

            print('M,A={a}'.format(a=attr))

            if hasattr(v, self.__META_PROPERTY):
                isOver = len(v.metaSelf) <= 0

                print('M-1,ISOVER={d},A={a}'.format(d=isOver, a=attr))

                if isOver:  # have not metaself property, is list or is scalars
                    _traverseLst(self, attr, v)
                else:
                    _traverse(v)  # have metaself, must be have dict
            else:
                _traverseLst(self, attr, v)
