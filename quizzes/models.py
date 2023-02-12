from django.db import models
from accounts.models import CustomUser

class Quiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    desc = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.desc

class Submission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.user.username + ' on ' + str(self.date_created)

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    body = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.body
