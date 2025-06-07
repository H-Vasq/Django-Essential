from django.urls import path

from . import views

urlpatters = [
    path('notes', views.list),
    path('', include('home.urls')),
    path('smart/', include('notes.urls')),
]