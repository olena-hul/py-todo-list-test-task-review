from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass
