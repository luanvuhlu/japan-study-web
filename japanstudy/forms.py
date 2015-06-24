# -*- coding: utf-8 -*-
from crispy_forms.templatetags.crispy_forms_field import css_class

__author__ = 'vuvanluan'
from django import forms
from django_select2.widgets import Select2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, ButtonHolder, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, UneditableField, StrictButton
from japanstudy.models import JapaneseWord, TestWord
class JapaneseWordAdvanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JapaneseWordAdvanceForm, self).__init__(*args, **kwargs)
        self.fields['source'].widget.attrs.update({'autofocus': 'autofocus'})
        self.helper = FormHelper(self)
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
        model = JapaneseWord
        exclude = ['user', 'active', 'created_time', 'temp']
class JapaneseWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JapaneseWordForm, self).__init__(*args, **kwargs)
        self.fields['source'].widget.attrs.update({'autofocus': 'autofocus'})
        self.helper = FormHelper(self)
        self.helper.form_id = 'addJPWords'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('source'),
            Field('mean'),
            Field('kanji'),
            Field('romaji'),
            Field('type'),
            Field('description', rows="3"),
        #     FormActions(
        #     Submit('save_changes', ' Add'),
        #     Submit('cancel', 'Cancel'),
        #     css_class='form-group',
        # )
    )
    class Meta:
        model = JapaneseWord
        fields = ['source', 'mean', 'kanji', 'romaji', 'type', 'description']
class TestWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestWordForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['start_date'].input_formats = ['%Y/%m/%d %H:%M']
        self.fields['completed_time'].input_formats = ['%Y/%m/%d %H:%M']
        self.helper = FormHelper(self)
        self.helper.form_id = 'testWordForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Field('title'),
            Field('words', css_class='picklist'),
            Field('start_date', css_class='datetimepicker' ),
            Field('completed_time' , css_class='datetimepicker' ),
            FormActions(
            Submit('save_changes', ' Add'),
            Submit('cancel', 'Cancel'),
            css_class='form-group',)
        )
    class Meta:
        model = TestWord
        fields = ['title', 'words', 'start_date', 'completed_time']
class TestingWordForm(forms.Form):
    def __init__(self, current=1,  end=None, source_val=None, mean_val=None, kanji_val=None, *args, **kwargs):
        super(TestingWordForm, self).__init__(*args, **kwargs)
        self.fields['mean'].widget.attrs.update({'autofocus': 'autofocus'})
        self.helper=FormHelper()
        self.helper.form_class="form-horizontal"
        self.helper.action="POST"
        if current==1 and end:
            form_submit_buttom= FormActions(
                                Submit('finish', 'Finish', css_class="btn-primary"),
                            )
        elif current==1:
            form_submit_buttom= FormActions(
                                Submit('next', 'Next', css_class="btn-primary"),
                            )
        elif end:
            form_submit_buttom= FormActions(
                                    Submit('prev', 'Prev'),
                                    Submit('finish', 'Finish', css_class="btn-primary"),
                                )
        else:
            form_submit_buttom= FormActions(
                                    Submit('prev', 'Prev'),
                                    Submit('next', 'Next', css_class="btn-primary"),
                                )
        self.helper.layout=Layout(
                             Field('source', value=source_val or '', disabled=True),
                             Field('mean', value=mean_val or ''),
                             Field('kanji', value=kanji_val or ''),
                             form_submit_buttom
                             )
    source=forms.CharField(max_length=200, required=False)
    mean=forms.CharField(max_length=200, required=False)
    kanji=forms.CharField(max_length=200, required=False)
    
    