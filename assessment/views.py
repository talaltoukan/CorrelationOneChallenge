from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Question, Candidate, QuestionAnswer, QuestionSessionResult
from .serializers import QuestionSerializer, CandidateSerializer, QuestionAnswerSerializer, QuestionSessionResultSerializer


# /questions/

class CandidateViewSet(viewsets.ModelViewSet):
    model = Candidate
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    model = QuestionAnswer
    serializer_class = QuestionAnswerSerializer
    queryset = QuestionAnswer.objects.all()


class QuestionSessionResultViewSet(viewsets.ModelViewSet):
    model = QuestionSessionResult
    serializer_class = QuestionSessionResultSerializer
    queryset = QuestionSessionResult.objects.all()


@api_view(['GET'])
def GetQuestion(request, uuid):
    question = Question.objects.get(pk=uuid)
    serializer = QuestionSerializer(question)
    response_data = serializer.data
    return Response(response_data, status=status.HTTP_200_OK)