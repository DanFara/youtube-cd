from django.db import models
from django.utils import timezone


class Profile(models.Model):
    profile = models.CharField(primary_key=True, max_length=200)
    total_points = models.FloatField(blank=True, null=True)
    participation = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']

class Session(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    total_responses = models.IntegerField(blank=True, null=True)
    youtube_session = models.CharField(max_length=10000)

    class Meta:
        ordering = ['timestamp']


class Question(models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=10000)
    solution = models.CharField(max_length=10000)
    time_limit = models.IntegerField()
    multiplier = models.IntegerField()
    to_receive = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['timestamp']

class Response(models.Model):

    original_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    response = models.FloatField(max_length=10000)
    value = models.FloatField()

    class Meta:
        ordering = ['timestamp']


