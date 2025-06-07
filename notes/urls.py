from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.list_notes, name='notes.list'),  # Added trailing slash
]

# urlpatterns = [
#     path('notes', views.list_notes, name='notes.list'),
#     path('', include('home.urls')),
#     path('smart/', include('notes.urls')),
# ]