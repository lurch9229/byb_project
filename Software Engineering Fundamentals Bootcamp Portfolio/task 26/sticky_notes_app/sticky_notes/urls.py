from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Added urls to load the notes app within the project and a redirect to notes/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='notes/', permanent=False)),
    path('notes/', include('notes.urls')),
    ]
