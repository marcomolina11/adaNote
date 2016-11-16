from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
class NoteManager(models.Manager):
	def adaNote(self, request):
		print "Entered adaNote function"
		list_order = self.filter(user_id=request.session['user_id']).count() + 1
		print list_order

		user_id = User.objects.get(id=request.session['user_id'])
		print user_id

		note = self.create(title=request.POST['title'], description=request.POST['description'], list_order=list_order, user_id=user_id)
		return (note, list_order)

	def deleteNote(self, request):
		print "Entered deleteNote function"
		# On delete we will update the list order of the note to be at the end.
		# list_order = self.filter(user_id=request.session['user_id']).count()
		# And update the delete field to be true
		self.filter(id=request.POST['id']).update(deleted=True, list_order=0)
		return (True, ["Note successfully marked as deleted"] )

	def updateTitle(self, request):
		print "Entered updateTitle function"
		# Use the note.id from the request to update that note's title
		self.filter(id=request.POST['id']).update(title=request.POST['title'])
		return (True, ["Note title updated"] )

	def updateDescription(self, request):
		print "Entered updateDescription function"
		# Use note.id from request to update that note's description
		self.filter(id=request.POST['id']).update(description=request.POST['description'])
		return (True, ["Note description updated"] )

class Note(models.Model):
	title = models.CharField(max_length=15)
	description = models.TextField(max_length=200)
	list_order = models.IntegerField(default=0)
	favorite = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	user_id = models.ForeignKey(User, related_name='usernote')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	noteManager = NoteManager()
	objects = models.Manager()

	class Meta:
		ordering = ['list_order']

	def __str__(self):
		return self.title

