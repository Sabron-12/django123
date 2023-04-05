from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField('Данные',max_length=100)
    task=models.TextField('Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Person(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    age=models.IntegerField()
    login=models.CharField(max_length=20)
    password=models.CharField(max_length=20)




