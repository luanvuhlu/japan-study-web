# -*- coding: utf-8 -*-
__author__ = 'vuvanluan'
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from japan.utils import get_user
from models import AddWordSession
from forms import JapaneseWordForm

@dajaxice_register
def add_new_words(request, form):
    user=get_user(request)
    dajax=Dajax()
    form=JapaneseWordForm(deserialize_form(form))
    if form.is_valid():
        word=form.save(commit=False)
        word.user=user
        word.temp=True
        word.save()
        add_word_session=AddWordSession.objects.get_or_create(current=True, active=True, user=user)
        add_word_session.save()
        add_word_session.japanese_words.add(word)
        dajax.remove_css_class('#addJPWords', 'error')
        # TODO
    else:
        dajax.remove_css_class('#addJPWords', 'error')
        for error in form.errors:
            dajax.add_css_class('#%s' % error, 'error')
    print(dajax.json())
    return dajax.json()
