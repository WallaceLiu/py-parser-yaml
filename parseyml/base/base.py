# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning800203@gmail.com

"""
import inspect


class Base(object):
    """
    基类
    """

    @property
    def clsName(self):
        return str(self.__class__.__name__)

    @clsName.setter
    def clsName(self, v):
        pass

    @property
    def fnName(self):
        return inspect.stack()[0][3]

    @fnName.setter
    def fnName(self, v):
        pass


class ReflectBase(Base):
    __meta = []

    def __init__(self):
        self.__metaSelf = []

    @property
    def meta(self):
        return self.__meta

    @meta.setter
    def meta(self, meta):
        if isinstance(meta, str) and meta not in self.__meta:
            self.__meta.append(meta)
        elif isinstance(meta, list):
            for m in meta:
                if m not in self.__meta:
                    self.__meta.append(m)

    @property
    def metaSelf(self):
        return self.__metaSelf

    @metaSelf.setter
    def metaSelf(self, meta):
        if isinstance(meta, str) and meta not in self.__metaSelf:
            self.__metaSelf.append(meta)
        elif isinstance(meta, list):
            for m in meta:
                if m not in self.__metaSelf:
                    self.__metaSelf.append(m)

    def getAttrObj(self, attr, o=None):
        """
        get object by attr
        :param attr:
        :param o:
        :return:
        """
        if o == None:
            return getattr(self,
                           attr,
                           '<{a}> Not Found in {f}.'.format(a=attr, f=self.clsName))
        else:
            return getattr(o,
                           attr,
                           '<{a}> Not Found in {f}.'.format(a=attr, f=self.clsName))

    def getAttrValue(self, attr, o=None):
        """
        get value of object by attr
        :param attr:
        :param o:
        :return:
        """
        v = self.getAttrObj(attr, o)

        return None if str(v).find("Not Found") > 0 else v

    def getAttrValueByDot(self, dot):
        """
        get value of object by attr dot
        :param dot:
        :return:
        """
        if dot is None:
            return None

        attrs = str(dot).split('.')
        # print(" **getAttrValueByDot {v}".format(v=attrs))
        if len(attrs) > 0:
            if len(attrs) == 1:
                val = self.getAttrValue(attrs[0])
                # print("     **getAttrValueByDot {v}".format(v=val))
                return val
            else:
                o = self.getAttrObj(attrs[0])
                po = o
                for i in range(len(attrs)):
                    if i >= 1:
                        o = self.getAttrObj(attrs[i], po)
                        po = o
                # print("     **getAttrValueByDot {v}".format(v=o))
                return o if str(o).find("Not Found") < 0 else None

        return None

    def setAttrValueByDot(self, attrDot):
        pass

    def setAttr(self, p, v, isCover=False):
        """
        set new attribute

        :except if attr exsited, so exception
        :param p:
        :param v:
        :return:
        """
        # if isCover == True:
        #     if hasattr(self, p):
        #         raise AttributeError(
        #                 'ERROR: setattr property={p},value={v} in {n}'.format(p=p,
        #                                                                       v=v,
        #                                                                       n=self.clsName))

        setattr(self, p, v)

    def setAttrId(self, id, parentId):
        """
        设置id和父id
        :param id:
        :param parentId:
        :return:
        """
        self.setAttr("id", id, True)
        self.setAttr("parent", parentId, True)
