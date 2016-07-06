#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
#! -*- coding: utf8 -*-
from trytond.pool import *
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pyson import Id
from trytond.report import Report
from trytond.transaction import Transaction
from trytond.modules.company import CompanyReport
from trytond.pool import Pool
from decimal import Decimal

__all__ = ['PriceListLine']

class PriceListLine():
    __metaclass__ = PoolMeta
    __name__ = 'product.price_list.line'

    percentage = fields.Numeric('Porcentaje de descuento')

    @classmethod
    def __setup__(cls):
        super(PriceListLine, cls).__setup__()
        cls.formula.states['readonly'] = Eval('active', True)

    @fields.depends('percentage', 'formula')
    def on_change_percentage(self):
        if self.percentage:
            if self.percentage > 0:
                percentage = self.percentage/100
                p = str(percentage)
            formula = 'unit_price * (1 - ' +p+')'
            self.formula = formula
