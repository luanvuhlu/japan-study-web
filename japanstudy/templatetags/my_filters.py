# -*- coding: utf-8 -*-
'''
Created on Jun 25, 2015

@author: luanvv
'''
from django import template

register=template.Library()

@register.filter()
def upfirstletter(value):
    value=value.strip() or ''
    first = value[0] if len(value) > 0 else ''
    remaining = value[1:] if len(value) > 1 else ''
    return first.upper() + remaining

