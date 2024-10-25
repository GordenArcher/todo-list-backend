from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path("sendtodo/", views.create_todo, name='sendtodo'),
    path('getalltodo/', views.getTodo, name='getalltodo')
]
