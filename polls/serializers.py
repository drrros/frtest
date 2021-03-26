from rest_framework import serializers
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response

from .models import Question, QuestionChoice, Answer, Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'description',
            'date_start',
            'date_end',
            'questions'
        ]
        depth = 1


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'type',
            'polls',
        ]

    def save(self, **kwargs):
        if self.instance.polls.exists():
            for poll in self.instance.polls.all():
                if poll.locked:
                    raise ValidationError(detail={
                        'error': 'Как минимум один из опросов заблокирован для изменений'
                    }
                    )
        return super().save(**kwargs)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'question',
            'userid',
            'value',
        ]

    def create(self, validated_data):
        answer, created = Answer.objects.update_or_create(
            question=validated_data.get('question'),
            userid=validated_data.get('userid'),
            defaults={'value': validated_data.get('value', '')})
        return answer


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = [
            'id',
            'text',
            'question',
        ]

    def save(self, **kwargs):
        if self.validated_data.get('polls', None):
            for poll in self.validated_data.get('polls'):
                if poll.locked:
                    raise ValidationError(detail={
                        'error': 'Как минимум один из опросов заблокирован для изменений'
                    }
                    )
        return super().save(**kwargs)
