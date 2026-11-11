from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('angler_posts/', views.angler_posts, name='angler_posts'),
    path('conservation_efforts/', views.conservation_efforts, name='conservation_efforts'),
]