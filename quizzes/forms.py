from django.forms import ModelForm
from .models import Quiz, Question, Submission, Answer

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["desc"]

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = []

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["body"]
