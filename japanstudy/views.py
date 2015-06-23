# -*- coding: utf-8 -*-
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.utils import timezone
from japanstudy.forms import JapaneseWordAdvanceForm, JapaneseWordForm, TestWordForm,\
    TestingWordForm
from japan.utils import get_user
from models import AddWordSession

import logging
from japanstudy.models import TestWord, TestSession, TestSessionWordOrder,\
    TestingWord
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
    return redirect('test-word-session', test_session_pk=test_session.id, order=1)
def test_word_session(request, test_session_pk, order):
    user=get_user(request)
    order=int(order)
    test_session=get_object_or_404(TestSession, pk=test_session_pk)
    word=test_session.test_session_word_orders.all()[order-1].word
    count_word=test_session.test_session_word_orders.all().count()
    if order <= 0 or order > count_word:
        raise Http404('Order invalid!')
    end = (order == count_word)
    
    if request.method == 'POST':
        testing_word, testing_word_created=TestingWord.objects.get_or_create(test_session=test_session, order=order, word=word)
        testing_word.source=request.POST.get('source')
        testing_word.mean=request.POST.get('mean')
        testing_word.kanji=request.POST.get('kanji')
        testing_word.save()            
        if request.POST.get('next') and not end:
            new_order=order+1
        elif request.POST.get('prev') and order>1:
            new_order=order-1
        elif request.POST.get('finish'):
            return redirect('test-word-session-result', test_session_pk=test_session.id)
        else:
            raise Http404('Invalid post!')
        return redirect('test-word-session', test_session_pk=test_session.id, order=new_order)
    else:
        try:
            testing_word_new=TestingWord.objects.get(test_session=test_session, order=order)
            form=TestingWordForm(current=order, end=end, source_val=word.source, mean_val=testing_word_new.mean, kanji_val= testing_word_new.kanji)
        except TestingWord.DoesNotExist:
            form=TestingWordForm(end=end, current=order, source_val=word.source)                 
    return render(request, 'japanstudy/testing.html',{
                                                      'username':user.username,
                                                      'form':form,
                                                    } )
def test_word_session_result(request, test_session_pk):
    
    pass
    
    