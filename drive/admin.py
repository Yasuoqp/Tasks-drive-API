from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'route', 'product', 'isActive', 'date', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')


admin.site.register(Task, TaskAdmin)
