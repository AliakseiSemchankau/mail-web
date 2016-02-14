from django.core.management import BaseCommand
from questions.models import Question
import random
import string
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):
    	for index in range(1, 200):
    		name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5, 20)))
    		text = ''.join(random.choice(string.ascii_lowercase + string.digits + string.whitespace) for _ in range(random.randint(10, 500)))
    		author_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    		like_count = random.choice([random.randint(0, 100), random.randint(0, 10), 2, 0, 1])
    		taglist = ['sql', 'web', 'java', 'socket', 'python', 'c-plus', 'c-sharp', 'c', 'anime', 'mikuru', 'swag', 'math', 'server',
    		'kek', 'movie', 'thread', 'uki', None, 'code', 'error', None, None, 'inheriting', 'haruhi']
    		tag1 = random.choice([
    			random.choice(taglist), 
    			None,  
    			''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(3, 7)))
    			])
    		tag2 = random.choice([
    			random.choice(taglist), 
    			None,  
    			''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(3, 7)))
    			])
    		tag3 = random.choice([
    			random.choice(taglist), 
    			None,  
    			''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(3, 7)))
    			])
    		question = Question(name=name, text=text)
    		question.author_id = author_id
    		question.like_count = like_count
    		question.tag1 = tag1
    		question.tag2 = tag2
    		question.tag3 = tag3
    		question.save();
        