#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from .price_list import *

def register():
    Pool.register(
        PriceListLine,
        module='nodux_product_price_list_percentage', type_='model')
