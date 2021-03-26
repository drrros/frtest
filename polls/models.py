from django.db import models


# Create your models here.

class Question(models.Model):
    TYPE_CHOICES = (
        ('text', 'Ответ текстом'),
        ('choice', 'Ответ выбором одного варианта'),
        ('multiple_choice', 'Ответ со многими вариантами'),
    )

    text = models.CharField(
        verbose_name='Текст вопроса',
        max_length=200
    )
    type = models.CharField(
        verbose_name='Тип вопроса',
        max_length=50,
        choices=TYPE_CHOICES,
    )

    def __str__(self):
        return f'{self.text}'




class Poll(models.Model):
    title = models.CharField(
        verbose_name='Название опроса',
        max_length=200,
    )
    description = models.CharField(
        verbose_name='Описание опроса',
        max_length=200,
    )
    date_start = models.DateTimeField(
        verbose_name='Дата начала проведения',
        blank=True,
        null=True,
    )
    date_end = models.DateTimeField(
        verbose_name='Дата окончания проведения',
        blank=True,
        null=True,
    )
    locked = models.BooleanField(
        verbose_name='Изменение вопросов заблокировано',
        default=False
    )
    questions = models.ManyToManyField(
        Question,
        related_name='polls',
        blank=True,
    )

    def __str__(self):
        return f'{self.title}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.date_start:
            self.locked = True
        super().save(force_insert, force_update, using, update_fields)


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )
    userid = models.PositiveIntegerField(
        verbose_name='ID пользователя'
    )
    value = models.TextField()

    def __str__(self):
        return f'{self.userid} - {self.value}'


class QuestionChoice(models.Model):
    text = models.CharField(
        verbose_name='Вариант ответа',
        max_length=200
    )
    question = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.question} - {self.text}'
