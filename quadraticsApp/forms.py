# from django.db import models
from django import forms
from .models import SettingsModel, TopicModel, SubTopicModel
from django.db import models
# from django.utils import timezone

class SettingsForm(forms.ModelForm):
    class meta:
        model = SettingsModel
        fields = ('id', 'creator', 'level1', 'level2', 'level3')

class TopicForm(forms.ModelForm):
    class Meta:
        model = TopicModel
        fields = ('id', 'topic')

class SubTopicForm(forms.ModelForm):
    class Meta:
        model = SubTopicModel
        fields = ('id', 'subtopic', 'topic')
