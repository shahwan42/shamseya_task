from django.contrib import admin

from shamseya_task.core.models import Answer, Choice, Question, Review

admin.site.register(Review)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Answer)
