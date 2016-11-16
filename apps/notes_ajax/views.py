from django.shortcuts import render, redirect
from models import Note
from forms import NoteForm 
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
class Welcome(View):
	def get(self, request):
		# Get all notes and render full index page with form

		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))

		context = {
			'notes': Note.objects.filter(user_id=request.session['user_id'], deleted=False),
			'new_note_form': NoteForm(),
		}
		return render(request, 'notes_ajax/index.html', context)

class Notes(View):
	def get(self, request):
		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))

		context = {
			'notes': Note.objects.filter(user_id=request.session['user_id'], deleted=False),
		}
		return render(request, 'notes_ajax/notes_index.html', context)

	def post(self, request):
		result = Note.noteManager.adaNote(request)
		note = result[0]
		list_order = result[1]
		print note.id
		print note.title
		print list_order
		return redirect(reverse('notes:notes'))

class Delete(View):
	def get(self, request):
		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))

		return redirect(reverse('notes:welcome'))

	def post(self, request):
		result = Note.noteManager.deleteNote(request)
		deleted = result[0]
		print result[1]
		print deleted
		return redirect(reverse('notes:notes'))

class UpdateDesc(View):
	def get(self, request):
		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))

		return redirect(reverse('notes:welcome'))

	def post(self, request):
		result = Note.noteManager.updateDescription(request)
		updated = result[0]
		print result[1]
		print updated
		return redirect(reverse('notes:notes'))

class UpdateTitle(View):
	def get(self, request):
		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))
		return redirect(reverse('notes:welcome'))

	def post(self, request):
		result = Note.noteManager.updateTitle(request)
		updated = result[0]
		print result[1]
		print updated
		return redirect(reverse('notes:notes'))

@method_decorator(csrf_exempt, name='dispatch')
class UpdateOrder(View):
	def get(self, request):
		if not 'user_id' in request.session:
			return redirect(reverse('login:index'))
		return redirect(reverse('notes:welcome'))

	def post(self, request):
		#Update the 'order' of all the notes. 
		for index, note_id in enumerate(request.POST.getlist('note[]')):
			Note.objects.filter(user_id=request.session['user_id'], id=int(str(note_id))).update(list_order=index+1)

		print "Update order request made"
		return redirect(reverse('notes:notes'))