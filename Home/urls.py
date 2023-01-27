from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.index, name='Home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("icecream", views.icecream, name='icecream'),
   path("doughnut", views.doughnut, name='doughnut'),
   path("softy", views.softy, name='softy'),




]
