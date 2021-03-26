# Generated by Django 2.2.10 on 2021-03-25 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст вопроса')),
                ('type', models.CharField(choices=[('text', 'Ответ текстом'), ('choice', 'Ответ выбором одного варианта'), ('multiple_choice', 'Ответ со многими вариантами')], max_length=50, verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Вариант ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='Вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название опроса')),
                ('description', models.CharField(max_length=200, verbose_name='Описание опроса')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала проведения')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания проведения')),
                ('locked', models.BooleanField(default=False, verbose_name='Изменение вопросов заблокировано')),
                ('questions', models.ManyToManyField(blank=True, related_name='polls', to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.PositiveIntegerField(verbose_name='ID пользователя')),
                ('value', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='Вопрос')),
            ],
        ),
    ]