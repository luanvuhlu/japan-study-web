# -*- coding: utf-8 -*-
__author__ = 'vuvanluan'
import json
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from forms import JapaneseWordForm
@dajaxice_register
def sayhello(request):
    return json.dumps({'message':'Hello World'})
@dajaxice_register
def add_new_words(request, form):
    dajax=Dajax()
    form=JapaneseWordForm(deserialize_form(form))
    if form.is_valid():
        dajax.remove_css_class('#addJPWords input', 'error')
        # TODO
    else:
        dajax.remove_css_class('#addJPWords input', 'error')
        for error in form.errors:
            dajax.add_css_class('#%s' % error, 'error')
    return dajax.json()
