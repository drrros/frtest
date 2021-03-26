from django.urls import path

from polls.views.admin import PollCreateAPIView, QuestionCreateAPIView, PollChangeAPIView, QuestionChangeAPIView, \
    PollListAdminAPIView, QuestionChoiceCreateAPIView, QuestionChoiceChangeAPIView
from polls.views.client import ActivePollAPIView, AnswerAPIView, GetAnswerAPIView

urlpatterns = [
    path('poll_list/', ActivePollAPIView.as_view(), name='active_polls_list_api'),
    path('answer/', AnswerAPIView.as_view(), name='answer_api'),
    path('get_answers/<int:userid>', GetAnswerAPIView.as_view(), name='get_answers_api'),
    path('admin/create_poll/', PollCreateAPIView.as_view(), name='poll_create_api'),
    path('admin/change_poll/<int:pk>', PollChangeAPIView.as_view(), name='poll_change_api'),
    path('admin/create_question/', QuestionCreateAPIView.as_view(), name='question_create_api'),
    path('admin/create_question_choice/', QuestionChoiceCreateAPIView.as_view(), name='question_choice_create_api'),
    path('admin/change_question/<int:pk>', QuestionChangeAPIView.as_view(), name='question_change_api'),
    path('admin/change_question_choice/<int:pk>', QuestionChoiceChangeAPIView.as_view(), name='question_choice_change_api'),
    path('admin/poll_list/', PollListAdminAPIView.as_view(), name='poll_list_admin_api'),
]
