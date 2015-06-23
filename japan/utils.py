# -*- coding: utf-8 -*-
from django.http.response import Http404
__author__ = 'vuvanluan'
def get_user(request):
    if request.user.is_authenticated():
        return request.user
    else:
        raise Http404('Not login!')