from django.urls import path
from . import views

# views based url imported by views
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
]