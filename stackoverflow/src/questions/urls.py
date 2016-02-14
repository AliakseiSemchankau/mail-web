from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /questions/
    url(r'^$', views.index, name='index'),
    # ex: /questions/ask
    url(r'^ask$', views.ask, name='ask'),
    # ex: /questions/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /questions/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /questions/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^answer/?$', views.answer, name='answer')
]

