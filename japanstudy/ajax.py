# -*- coding: utf-8 -*-
__author__ = 'vuvanluan'
import json
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from japan.utils import get_user
from forms import JapaneseWordForm
from models import JapaneseWord

@dajaxice_register
def add_new_words(request, form):
    user=get_user(request)
    dajax=Dajax()
    form=JapaneseWordForm(deserialize_form(form))
    if form.is_valid():
        word=form.save(commit=False)
        word.user=user
        word.save()
        dajax.remove_css_class('#addJPWords input', 'error')
        # TODO
    else:
        dajax.remove_css_class('#addJPWords input', 'error')
        for error in form.errors:
            dajax.add_css_class('#%s' % error, 'error')
    print(dajax.json())
    return dajax.json()
