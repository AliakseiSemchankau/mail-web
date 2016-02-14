from .models import Question
from .models import Answer
from django import forms

import datetime

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('name', 'text', 'tag1', 'tag2', 'tag3')

    # def clean_name(self):
    # 	if self.cleaned_data['name'] is None:
    # 		raise forms.ValidationError(u'You forgot to enter the name')
    # 	return self.cleaned_data
    # def clean_text(self):
    # 	if self.cleaned_data['text'] is None:
    # 		raise forms.ValidationError(u'You forgot to enter the text')
    #     return self.cleaned_data

    def is_valid(self):
    	return True

    # def save(self):
    #     self.pub_date = datetime.datetime.now()
    #     super(QuestionForm, self).save()

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text',)

    def is_valid(self):
    	return True

    



