from django.conf.urls import url
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register('candidate', views.CandidateViewSet)
router.register('question', views.QuestionViewSet)
router.register('question-answer', views.QuestionAnswerViewSet)
router.register('question-session-result', views.QuestionSessionResultViewSet)

urlpatterns =[
    url(r'^questions/(?P<pk>[0-9]+)/$', views.GetQuestion, name='question-detail'),
] + router.urls
