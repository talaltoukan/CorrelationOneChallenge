from rest_framework import serializers
import datetime
from django.utils import timezone
from .models import Candidate, Question, QuestionAnswer, Session, QuestionSessionResult


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        exclude = []


class NestedQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        exclude = ['correct']


class SessionSerializer(serializers.ModelSerializer):

    is_expired = serializers.SerializerMethodField()
    has_completed_all_questions = serializers.SerializerMethodField()

    def get_has_completed_all_questions(self, obj):
        num_questions = Question.objects.all().count()
        num_users_answered_questions = obj.questionsessionresult_set.all().count()

        return num_questions == num_users_answered_questions

    def get_is_expired(self, obj):
        one_hour_ago = timezone.now() + datetime.timedelta(hours=-1)
        return obj.started_at < one_hour_ago

    class Meta:
        model = Session
        exclude = []


class CandidateSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True, source='session_set')

    class Meta:
        model = Candidate
        exclude = []


class QuestionSerializer(serializers.ModelSerializer):

    answers = NestedQuestionAnswerSerializer(many=True, read_only=True, source='answer_choices')

    class Meta:
        model = Question
        fields = '__all__'

class QuestionSessionResultSerializer(serializers.ModelSerializer):

    is_correct = serializers.BooleanField(read_only=True)

    class Meta:
        model = QuestionSessionResult
        exclude = []
