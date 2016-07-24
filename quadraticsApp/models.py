from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# from django import forms

class TopicModel(models.Model):
    topic = models.CharField(max_length = 100)

    def __str__(self):              # __unicode__ on Python 2
        return self.topic

class SubTopicModel(models.Model):
    subtopic = models.CharField(max_length = 100)
    topic = models.ForeignKey(TopicModel)

    def __str__(self):              # __unicode__ on Python 2
        return self.subtopic

class SettingsModel(models.Model):
    creator = models.ForeignKey(User)
    topicid = models.ForeignKey(TopicModel)
    subtopicid = models.ForeignKey(SubTopicModel)
    level1 = models.IntegerField(default=3)
    level2 = models.IntegerField(default=3)
    level3 = models.IntegerField(default=3)

    def __str__(self):              # __unicode__ on Python 2
        return 'Creator, ' + str(self.creator)
