from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.login.urls', namespace='login')),
    url(r'^users/', include('apps.notes_ajax.urls', namespace='notes')),
]
