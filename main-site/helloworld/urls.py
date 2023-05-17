from django.urls import path
from helloworld import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]