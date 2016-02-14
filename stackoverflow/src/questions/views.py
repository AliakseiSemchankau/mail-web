from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from .forms import QuestionForm
from .forms import AnswerForm
from .models import Question, Tag, Answer
from loginsys.views import login

from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.contrib.auth.models import User
from loginsys.models import UserProfile
import sys

import inspect

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     return render(request, '../templates/main.html', {
#         'question_list':latest_question_list,
#     })



def index(request):


    page = request.GET.get('page')

    if page is None:
        page = 1

    sort_method = request.GET.get('sort')

    if sort_method is None:
        sort_method = 'pub_date'

    correctsort = '&sort=' + sort_method

    try:
        sort = '' + sort_method
    except:
        sort = 'pub_date'

    questions = Question.objects.all()

    if sort == 'tag':
        
        tag = request.GET.get('tag')
        correctsort = correctsort + '&tag=' + tag;
        questions = questions.filter(
            Q(tag1 = tag) | Q(tag2 = tag) | Q(tag3 = tag)
        )
        sort = 'pub_date'

    questions = questions.order_by('-' + sort)

    paginator = Paginator(questions, 20)

    try:
        question_list = paginator.page(page)
    except PageNotAnInteger: 
        question_list = paginator.page(1)
    except EmptyPage:
        question_list = paginator.page(paginator.num_pages)

    users = UserProfile.objects.all()
    #print users.get(pk=3).avatar.url
    #sys.stdout.flush()

    return render(request, '../templates/main.html', {
        'question_list':question_list, 'sort':correctsort, 'users':users ,
    })


def ask(request):
  
    # if request.user.is_authenticated() == False:
    #     return login(request)

    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    asked = False

    # print inspect.getmembers(QuestionForm, predicate=inspect.ismethod)

    pkid = 0

    # If it's ons/views.py in <module>, line 81a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        question_form = QuestionForm(data=request.POST)

        # If the two forms are valid...
        if question_form.is_valid():

            user = UserProfile.objects.all().get(user_id=request.user.pk)

            # Save the user's form data to the database
            question = question_form.save()
            question.author_id = user.pk
            question.save()

            pkid = question.pk

            tag_name1 = question.tag1
            try :
                taglist1 = Tag.objects.get(tag_name=tag_name1)
                taglist1.questions.add(question)
                taglist1.save()
            except Tag.DoesNotExist:
                newtag1 = Tag(tag_name=tag_name1)
                newtag1.save()
                newtag1.questions.add(question)
                newtag1.save()

            tag_name2 = question.tag2
            try :
                taglist2 = Tag.objects.get(tag_name=tag_name2)
                taglist2.questions.add(question)
                taglist2.save()
            except Tag.DoesNotExist:
                newtag2 = Tag(tag_name=tag_name2)
                newtag2.save()
                newtag2.questions.add(question)
                newtag2.save()
           
            tag_name3 = question.tag3
            try :
                taglist3 = Tag.objects.get(tag_name=tag_name3)
                taglist3.questions.add(question)
                taglist3.save()
            except Tag.DoesNotExist:
                newtag3 = Tag(tag_name=tag_name3)
                newtag3.save()
                newtag3.questions.add(question)
                newtag3.save()

            # Update our variable to tell the template registration was successful.
            asked = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return render_to_response(
                'askQuestion.html',
                {'question_form': question_form, 'asked': asked, 'form':question_form},
                context)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        return render_to_response(
                'askQuestion.html',
                {'asked': asked},
                context)

    # Render the template depending on the context.
    if asked == False:
        return render_to_response(
                'askQuestion.html',
                {'question_form': question_form, 'asked': asked},
                context)
    else:
        return redirect('/questions/' + str(pkid))

def answer(request):
    context = RequestContext(request)
    answered = False
    qid = 0
    aid = 0

    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)

        print 'first if'
        sys.stdout.flush()

        if answer_form.is_valid():
            user = UserProfile.objects.all().get(user_id=request.user.pk)

            # Save the user's form data to the database
            answer = answer_form.save()
            answer.author_id = user.pk
            answer.question_id = request.GET.get('q')
            answer.save()

            print 'success save!'
            sys.stdout.flush()
            aid = answer.pk
            qid = answer.question_id
           
            question = Question.objects.all().get(pk=qid)
            question.answer_count = question.answer_count + 1
            question.save()

            # Update our variable to tell the template registration was successful.
            answered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print 'first else('
            sys.stdout.flush()
            return render_to_response(
                'questionRegistered.html',
                {'answer_form': answer_form, 'answered': answered, 'form':answer_form},
                context)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        return render_to_response(
                'questionRegistered.html',
                {'answered': answered},
                context)

    # Render the template depending on the context.
    if answered == False:
        return render_to_response(
                'questionRegistered.html',
                {'answer_form': answer_form, 'answered': answered},
                context)
    else:
        return redirect('/questions/' + str(qid))

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.all().filter(question_id = question_id)
    return render(request, '../templates/questionRegistered.html', {'question': question, 'answers': answers})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



# Leave the rest of the views (detail, results, vote) unchanged
