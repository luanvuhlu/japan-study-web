# -*- coding: utf-8 -*-
__author__ = 'vuvanluan'
def get_user(request):
    if request.user.is_authenticated():
        return request.user