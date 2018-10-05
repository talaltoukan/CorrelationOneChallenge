# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

MULTIPLE_CHOICE_ANSWERS = (('A',"A"),('B',"B"),('C',"C"),('D',"D"),('E',"E"))

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def save(self, *args, **kwargs):
        candidate_exists = True
        if not self.pk:
            candidate_exists = False
        super(Candidate, self).save(*args, **kwargs)

        if not candidate_exists:
            Session.objects.create(candidate=self)

    def __str__(self):
        return self.first_name + self.last_name


class Session(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    started_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.question


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_choices')
    answer = models.CharField(choices=MULTIPLE_CHOICE_ANSWERS, max_length=1)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    correct = models.BooleanField(default=False)


class QuestionSessionResult(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    answer = models.CharField(choices=MULTIPLE_CHOICE_ANSWERS, max_length=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ['session', 'question']

    def save(self,  *args, **kwargs):
        correct_answer = self.question.answer_choices.filter(correct=True).first()
        # Records whether candidate's choice is correct or not
        if correct_answer and correct_answer.answer == self.answer:
            self.is_correct = True

        super(QuestionSessionResult, self).save(*args, **kwargs)
