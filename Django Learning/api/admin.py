from django.contrib import admin
from .models import TodoList

class AdminTodoList(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed')
    search_fields = ('title',)
    list_per_page = 10
    list_editable = ('is_completed',)

admin.site.register(TodoList, AdminTodoList)