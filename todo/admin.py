from django.contrib import admin
from .models import TodoTable

# Register your models here.

class TodoTableAdmin(admin.ModelAdmin):
    list_display = ['user', 'todo', 'date_created']
    search_fields = ['user', 'todo', 'date_created']

    def __str__(self):
        return self.user
    


admin.site.register(TodoTable, TodoTableAdmin)
