from django.contrib import admin
from tasks.models import TasksItem, TasksList

admin.site.register(TasksItem)
admin.site.register(TasksList)
