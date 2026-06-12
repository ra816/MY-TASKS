from django.contrib import admin
from .models import Todo, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'color')
    list_filter = ('user',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'due_date', 'completed', 'created_at')
    list_filter = ('completed', 'priority', 'category', 'user')
    search_fields = ('title', 'description')
