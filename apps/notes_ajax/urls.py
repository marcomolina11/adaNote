from django.conf.urls import url
from django.contrib import admin


from views import Welcome, Notes, Delete, UpdateDesc, UpdateTitle, UpdateOrder


urlpatterns = [
	url(r'^update_title$', UpdateTitle.as_view(), name='update_title'),
	url(r'^update_desc$', UpdateDesc.as_view(), name='update_desc'),
	url(r'^notes$', Notes.as_view(), name='notes'),
	url(r'^delete$', Delete.as_view(), name='delete'),
	url(r'^update_order$', UpdateOrder.as_view(), name='update_order'),
	url(r'^$', Welcome.as_view(), name='welcome'),
]