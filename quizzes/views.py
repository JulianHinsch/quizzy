from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

from .forms import QuizForm, QuestionForm, SubmissionForm, AnswerForm
from .models import Quiz, Question, Submission, Answer

def quiz_list(request):
    context = {'quizzes': Quiz.objects.all()}
    return render(request, 'quizzes/quiz_list.html', context)

def quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id = quiz_id)
    if request.method == 'POST':
        user = request.user
        sf = SubmissionForm(request.POST,
            instance = Submission(user=user))
        afs = [
            AnswerForm(request.POST, prefix = str(x), instance = Answer()) for x in range(0, len(request.POST) - 1)
        ]
        if sf.is_valid() and all([af.is_valid() for af in afs]):
            new_submission = sf.save(commit=False)
            new_submission.user = request.user
            new_submission.quiz = quiz
            new_submission.save()
            for index, value in enumerate(afs):
                new_answer = value.save(commit=False)
                new_answer.quiz = quiz
                new_answer.question = quiz.question_set.all()[index]
                new_answer.submission = new_submission
                new_answer.user = request.user
                new_answer.save()
            return HttpResponseRedirect('/quizzes/complete')
    elif request.method == 'DELETE':
        Quiz.objects.filter(pk=quiz.id).delete()
    else:
        num_of_questions = len(quiz.question_set.all())
        sf = SubmissionForm()
        afs = [
            AnswerForm(prefix = str(x),
                instance = Answer()) for x in range(0, num_of_questions)
        ]
        context = {
            'quiz': quiz,
            'submission_form': sf,
            'answer_forms_questions': zip(afs, quiz.question_set.all()),
        }
        return render(request, 'quizzes/quiz_detail.html', context)

def complete(request):
    return render(request, 'quizzes/complete.html')

@login_required
def account(request):
    context = {'quizzes': Quiz.objects.filter(user=request.user)}
    return render(request, 'quizzes/account.html', context)

@login_required
def submissions(request, quiz_id):
    quiz = get_object_or_404(Quiz, id = quiz_id)
    context = {
        'quiz': quiz,
        'submissions': quiz.submission_set.all()
    }
    return render(request, 'quizzes/submission_list.html', context)

@login_required
def submission_detail(request, quiz_id, submission_id):
    quiz = get_object_or_404(Quiz, id = quiz_id)
    submission = get_object_or_404(Submission, id = submission_id)
    answers = submission.answer_set.all()
    context = {'quiz': quiz, 'submission': submission, 'answers': answers}
    return render(request, 'quizzes/submission_detail.html', context)

@login_required
def new_quiz(request):
    if request.method == 'POST':
        user = request.user
        quiz_form = QuizForm(request.POST, instance = Quiz(user = user))
        question_forms = [
            QuestionForm(request.POST, prefix = str(x),
            instance = Question()) for x in range(0, len(request.POST) - 2)
        ]
        if quiz_form.is_valid() and all([question_form.is_valid() for question_form in question_forms]):
            new_quiz = quiz_form.save(commit=False)
            new_quiz.user = request.user
            new_quiz.save()
            for question_form in question_forms:
                new_question = question_form.save(commit=False)
                new_question.quiz = new_quiz
                new_question.user = request.user
                new_question.save()
            return HttpResponseRedirect('/quizzes/%s' % new_quiz.id)
    else:
        quiz_form= QuizForm()
        question_forms = [QuestionForm(prefix = str(x), instance = Question()) for x in range(0,3)]
        context = {'quiz_form': quiz_form, 'question_forms': question_forms}
        return render(request, 'quizzes/new_quiz.html', context)