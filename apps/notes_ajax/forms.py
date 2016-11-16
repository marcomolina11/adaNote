from django import forms
from .models import Note

class NoteForm(forms.Form):
	title = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder':'Enter note title...'}), label="")
	description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder':'Write a note...'}), label="")

