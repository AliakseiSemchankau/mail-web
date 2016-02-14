from django.core.management import BaseCommand
from questions.models import Question, Answer
import random
import string
import sys
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):
        questions = Question.objects.all()
        answers = Answer.objects.all()
    	for question in questions:
            qanswers = answers.filter(question_id = question.pk)
            question.answer_count = qanswers.count()
            question.save()
            print question.pk
            sys.stdout.flush()
        