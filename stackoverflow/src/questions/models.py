from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime

from loginsys.models import UserProfile
from django.contrib.auth.models import User

class Question(models.Model):

    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(UserProfile, null=True)
    answer_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    tag1 = models.CharField(max_length = 10, null=True, blank=True)
    tag2 = models.CharField(max_length = 10, null=True, blank=True)
    tag3 = models.CharField(max_length = 10, null=True, blank=True)
    #likers = models.ManyToManyField(User)

    def __str__(self):              # __unicode__ on Python 2
        return self.text

class Tag(models.Model):

	tag_name = models.CharField(max_length = 10)
	questions = models.ManyToManyField(Question)


class Answer(models.Model):

    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    author = models.ForeignKey(UserProfile, null=True)
    question = models.ForeignKey(Question, null=True)
    like_count = models.IntegerField(default=0)


