from django.contrib import admin
from .models import SettingsModel, TopicModel, SubTopicModel
from .forms import SettingsForm, TopicForm, SubTopicForm

class SettingsModelAdmin(admin.ModelAdmin):
    form = TopicForm
    fields = ('creator', 'topicid', 'subtopicid', 'level1', 'level2', 'level3')
    # pass
    list_display = ['id', 'creator', 'topicid', 'subtopicid', 'level1', 'level2', 'level3']

admin.site.register(SettingsModel, SettingsModelAdmin)

class TopicModelAdmin(admin.ModelAdmin):
    form = TopicForm
    fields = ('topic',)
    # pass
    list_display = ['id', 'topic']

admin.site.register(TopicModel, TopicModelAdmin)

class SubTopicModelAdmin(admin.ModelAdmin):
    form = SubTopicForm
    fields = ('subtopic', 'topic')
    # pass
    list_display = ['id', 'subtopic', 'topic']

admin.site.register(SubTopicModel, SubTopicModelAdmin)
