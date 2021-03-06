# -*- coding: utf-8 -*-
from . import attribute


class ID(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('IDがNoneです')
        if attr < 0 or type(attr) is not int:
            raise Exception('IDは0以上の整数を指定してください')
