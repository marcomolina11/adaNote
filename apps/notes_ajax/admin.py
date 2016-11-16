from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
	list_display = ('title', 'id', 'list_order', 'user_id')
	list_filter = ['user_id']

admin.site.register(Note, NoteAdmin)
