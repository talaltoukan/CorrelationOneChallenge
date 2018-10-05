# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Candidate, Question, QuestionAnswer, QuestionSessionResult
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


# Create your tests here.
class CandidateTestCase(TestCase):

    def createCandidate(self):
        first_name = "Kanye"
        last_name = "West"
        email = "yeezy@gmail.com"
        return Candidate.objects.create(first_name=first_name, last_name=last_name, email=email)


    def test_candidate_create(self):
        c = self.createCandidate()
        self.assertTrue(isinstance(c, Candidate))
        self.assertEqual(c.first_name, "Kanye")


class QuestionTestCase(TestCase):

    def createQuestion(self):
        quest = "What is the capital of Texas?"
        return Question.objects.create(question=quest)

    def test_question_create(self):
        q = self.createQuestion()
        self.assertTrue(isinstance(q, Question))
        self.assertEqual(q.__str__(), "What is the capital of Texas?")


class QuestionAnswerTestCase(TestCase):
    def createWrongQuestionAnswer(self):
        qObj = Question.objects.create(question="What is the capital of Texas?")
        return QuestionAnswer.objects.create(question=qObj, answer='A', text='New York City')

    def createRightQuestionAnswer(self):
        qObj = Question.objects.create(question="What is the capital of Texas?")
        return QuestionAnswer.objects.create(question=qObj, answer='A', text='Austin', correct=True)

    def test_question_answers(self):
        wrong = self.createWrongQuestionAnswer()
        right = self.createRightQuestionAnswer()
        self.assertTrue(isinstance(wrong, QuestionAnswer))
        self.assertTrue(isinstance(right, QuestionAnswer))
        self.assertEqual(wrong.text, "New York City")
        self.assertEqual(right.text, "Austin")
        self.assertFalse(wrong.correct)
        self.assertTrue(right.correct)