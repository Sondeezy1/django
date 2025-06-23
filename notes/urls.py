from django.urls import path
from . import views

from .views import CustomLoginView, RegisterView
from .views import logout_get_view
from .views import landing_page


urlpatterns = [
    path('home/', views.home, name='home'),
    path('edit/<int:pk>/', views.note_update, name='note_update'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_get_view, name='logout'),
    path('edit/<int:pk>/', views.note_update, name='note_update'),
    path('', landing_page, name='landing'),
    path('edit/<int:pk>/', views.note_update, name='note_update'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/create/', views.note_create, name='note_create'),
    
]
