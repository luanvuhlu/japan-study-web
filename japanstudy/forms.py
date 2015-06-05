# -*- coding: utf-8 -*-
from crispy_forms.templatetags.crispy_forms_field import css_class

__author__ = 'vuvanluan'
from django import forms
from django_select2.widgets import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, ButtonHolder, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, UneditableField, StrictButton
from japanstudy.models import JapaneseWord
class JapaneseWordAdvanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JapaneseWordAdvanceForm, self).__init__(*args, **kwargs)
        self.helper=FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.error_text_inline = True
        self.helper.layout = Layout(
            Field('source'),
            Field('mean'),
            Field('kanji'),
            Field('romaji'),
            Field('type'),
            Field('other_mean'),
            Field('example'),
            Field('description'),
            Field('sames'),
            Field('level'),
            Field('tags'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="col-lg-offset-2 btn-primary"),
            Submit('cancel', 'Cancel'),
            css_class='form-group',
        )
    )
    class Meta:
        model=JapaneseWord
        exclude=['user', 'active', 'created_time']
class JapaneseWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JapaneseWordForm, self).__init__(*args, **kwargs)
        self.helper=FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Field('source'),
            Field('mean'),
            Field('kanji'),
            Field('romaji'),
            Field('type'),
    )
    class Meta:
        model=JapaneseWord
        fields=['source', 'mean', 'kanji', 'romaji', 'type']