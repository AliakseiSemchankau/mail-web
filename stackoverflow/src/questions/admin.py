from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question
from .models import Tag
from .models import Answer

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class AnswerAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'text', 'question_id']

admin.site.register(Question)
admin.site.register(Answer)

