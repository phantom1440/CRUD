from django.urls import path 
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('delete/<pk>', views.delete, name='delete'),
    path('update/<pk>', views.update, name='update'),
]