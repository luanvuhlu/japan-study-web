# -*- coding: utf-8 -*-
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.utils import timezone
from japanstudy.forms import JapaneseWordAdvanceForm, JapaneseWordForm, TestWordForm
from japan.utils import get_user
from models import AddWordSession

import logging
from japanstudy.models import TestWord, TestSession, TestSessionWordOrder
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
def add_word_success(request):
    return HttpResponse('success')
def add_test_case(request):
    user = get_user(request)
    if request.method == 'POST':
        form = TestWordForm(request.POST)
        if form.is_valid():
            test_word = form.save(commit=False)
            test_word.user = user
            test_word.save()
            form.save_m2m()
            form = TestWordForm()
        else:
            # TODO
            log.error(form.errors)
    else:
        form=TestWordForm()
    return render(request, 'japanstudy/add-test-case-word.html', {
        'username':user.username,
        'form':form
    })
class TestWordListView(ListView):
    model=TestWord
    def get_context_data(self, **kwargs):
        context=super(TestWordListView, self).get_context_data(**kwargs)
        return context
def start_test_word(request, pk):
    test_word=get_object_or_404(TestWord, pk=pk)
    words=test_word.get_shuffle_words()
    test_session=TestSession.objects.create(test_word=test_word, user=get_user(request))
    test_session.save()
    for i in range(1, len(words)):
        test_session_word_order=TestSessionWordOrder.objects.create(order=i, word=words[i])
        test_session_word_order.save()
        test_session.test_session_word_orders.add(test_session_word_order)
    return redirect('test-word-session', test_session=test_session.id, word=1)
def test_word_session(request, test_session, word):
    test_session=get_object_or_404(TestSession, pk=test_session)
    for w in test_session.test_session_word_orders.all():
        w.current=False
        if w.order==word:
            w.current=True
        if not w.completed:
            w.start=timezone.now()
        w.save()
    return HttpResponse('start')