# Generated by Django 3.0.8 on 2020-08-07 21:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quora', '0007_question_favourite_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='favourite_post',
        ),
        migrations.AddField(
            model_name='question',
            name='favourite_ques',
            field=models.ManyToManyField(blank=True, related_name='favourite_ques', to=settings.AUTH_USER_MODEL),
        ),
    ]
