from django.utils import timezone
from rest_framework import generics

from polls.models import Poll, Answer
from polls.serializers import PollSerializer, AnswerSerializer


class ActivePollAPIView(generics.ListAPIView):
    serializer_class = PollSerializer

    def get_queryset(self):
        return Poll.objects.filter(
            date_start__lt=timezone.now(),
            date_end__gt=timezone.now()
        )


class AnswerAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer


class GetAnswerAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(userid=self.kwargs['userid'])
