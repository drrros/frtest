from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from polls.models import Poll, Question, QuestionChoice
from polls.serializers import PollSerializer, QuestionSerializer, QuestionChoiceSerializer


class PollCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PollSerializer


class PollChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class QuestionCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer


class QuestionChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class PollListAdminAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class QuestionChoiceCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionChoiceSerializer


class QuestionChoiceChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionChoiceSerializer
    queryset = QuestionChoice.objects.all()
