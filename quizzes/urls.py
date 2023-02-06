from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('new', views.new_quiz, name='new_quiz'),
    path('complete', views.complete, name='complete'),
    path('<quiz_id>', views.quiz, name='quiz_detail'),
    path('<quiz_id>/submissions', views.submissions, name='submissions'),
    path('<quiz_id>/submissions/<submission_id>', views.submission_detail, name='submission_detail')
]
