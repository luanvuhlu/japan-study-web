# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render
from japanstudy.forms import JapaneseWordAdvanceForm, JapaneseWordForm
from japan.utils import get_user
from models import AddWordSession
import logging
log = logging.getLogger(__name__)
# Create your views here.
def home(request):
    form = JapaneseWordAdvanceForm()
    return render(request, "japanstudy/index.html", {
        'form':form,
    })
def add_japan_word_advance(request):
    user = get_user(request)
    if request.method == 'POST':
        form = JapaneseWordAdvanceForm(request.POST)
        if form.is_valid():
            log.debug('valid')
            word = form.save(commit=False)
            word.user = user
            word.save()
            # form=JapaneseWordAdvanceForm(instance=word)
            form = JapaneseWordAdvanceForm()
        else:
            # TODO
            log.error(form.errors)
            # form=JapaneseWordAdvanceForm()
    else:
        form = JapaneseWordAdvanceForm()
    return render(request, 'japanstudy/add-jp-word-advance.html', {
        'username':user.username,
        'form':form,

    })
def add_japan_word(request):
    user = get_user(request)
    if request.method != 'POST':
        for session in AddWordSession.objects.filter(current=True, active=True, user=user):
            session.current = False
            session.save() 
        form = JapaneseWordForm()
    else:
        form = JapaneseWordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.user = user
            word.temp = True
            word.save()
            # form=JapaneseWordAdvanceForm(instance=word)
            form = JapaneseWordForm()
        else:
            # TODO
            log.error(form.errors)
            # form=JapaneseWordAdvanceForm()       
    return render(request, 'japanstudy/add-jp-word.html', {
        'username':user.username,
        'form':form
    })


