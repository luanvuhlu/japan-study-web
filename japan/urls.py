"""japan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
import settings
from japanstudy.views import TestWordListView, TestingWordResultView, TestSessionListView
admin.autodiscover()
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = [
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^add-word$', 'japanstudy.views.add_japan_word', name='add-japan-word'),
    url(r'add-word-advance', 'japanstudy.views.add_japan_word_advance2', name='add-japan-word-advance'),
    url(r'^$', 'japanstudy.views.home', name='home'),
    url(r'^add-word-success', 'japanstudy.views.add_word_success', name='add_word_success'),
    url(r'^add-test-case', 'japanstudy.views.add_test_case', name='add-test-case'),
    url(r'^test-cases', TestWordListView.as_view(), name='test-cases-list'),
    url(r'^start-test-word/(?P<pk>\d+)', 'japanstudy.views.start_test_word', name='start-test-word'),
    url(r'^test-word/(?P<test_session_pk>\d+)/(?P<order>\d+)', 'japanstudy.views.test_word_session', name='test-word-session'),
    url(r'^test-word-result/(?P<test_session_pk>\d+)', TestingWordResultView.as_view(), name='test-word-session-result'),
    url(r'^test-session-list', TestSessionListView.as_view(), name='test-session-list'),
]
# STATIC
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
# MEDIA
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))
