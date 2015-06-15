# -*- coding: utf-8 -*-
__author__ = 'vuvanluan'
import json
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from dajax.core import Dajax
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from japan.utils import get_user
from models import AddWordSession, JapaneseWord
from forms import JapaneseWordForm


@dajaxice_register
def add_new_words(request, form):
    user = get_user(request)
#     dajax=Dajax()
    form = JapaneseWordForm(deserialize_form(form))
    if form.is_valid():
        word = form.save(commit=False)
        if len(JapaneseWord.objects.filter(source=word.source, mean=word.mean )):
            # TODO show error
            return None
        word.user = user
        word.temp = True
        word.save()
        add_word_session, created = AddWordSession.objects.get_or_create(current=True, active=True, user=user)
        if created:
            add_word_session.save()
        add_word_session.japanese_words.add(word)
        return render(request, 'japanstudy/new-word-ajax.html', {'word':word, })
#         dajax.remove_css_class('#addJPWords', 'success')
        # TODO
    else:
#         dajax.remove_css_class('#addJPWords', 'error')
        for error in form.errors:
            # TODO
            pass
#             dajax.add_css_class('#%s' % error, 'error')
        return None
#     return dajax.json()
@dajaxice_register()
def save_session(request):
    user = get_user(request)
    add_word_session = get_object_or_404(AddWordSession, current=True, active=True, user=user)
    add_word_session.current = False
    add_word_session.save()
    for word in add_word_session.japanese_words.all():
        word.temp = False
        word.save()
    return True
