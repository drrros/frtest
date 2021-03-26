from django.contrib import admin

# Register your models here.
from polls.models import Question, Poll, QuestionChoice, Answer

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Answer)
admin.site.register(QuestionChoice)
