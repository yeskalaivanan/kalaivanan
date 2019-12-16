# from django.conf.urls import url
from django.urls import path
from second_app import views

urlpatterns=[
    path('', views.index, name='index'),
]
