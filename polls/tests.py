from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Poll, Answer, Question, QuestionChoice
from .serializers import PollSerializer


class PollTest(APITestCase):
    """ Test module for test polls API """

    def setUp(self):
        User.objects.create_superuser(username='admin', email='admin@drros.ru', password='123AdminPassword')
        poll = Poll.objects.create(
            title='Poll',
            description='Poll desc',
        )
        question = Question.objects.create(
            text='Question',
            type='text'
        )
        QuestionChoice.objects.create(
            text='QC',
            question=question
        )
        QuestionChoice.objects.create(
            text='QC2',
            question=question
        )
        poll.questions.add(question)

    def testTasks(self):
        user = User.objects.get(username='admin')
        url = reverse('poll_list_admin_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        poll = Poll.objects.filter(id=1)
        serialized_poll = PollSerializer(poll, many=True)
        self.assertEqual(response.data, serialized_poll.data)

        url = reverse('question_change_api', kwargs={'pk': 1})
        response = self.client.patch(url, data={'text': 'asdqwe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(poll.first().questions.first().text, 'asdqwe')

        url = reverse('poll_change_api', kwargs={'pk': 1})
        response = self.client.put(url, data={
            'date_start': timezone.now(),
            'title': 'Poll',
            'description': 'Poll desc',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('question_change_api', kwargs={'pk': 1})
        response = self.client.patch(url, data={'text': 'text'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.client.logout()
        self.assertEqual(Answer.objects.count(), 0)
        url = reverse('answer_api')
        data = {
            'question': 1,
            'userid': 123,
            'value': 'asd'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(Answer.objects.get().userid, 123)
        self.assertEqual(Answer.objects.get().value, 'asd')

        url = reverse('get_answers_api', kwargs={'userid': 123})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['question'], 1)
        self.assertEqual(response.data[0]['userid'], 123)
        self.assertEqual(response.data[0]['value'], 'asd')
