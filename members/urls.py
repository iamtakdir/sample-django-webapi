from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('team/', views.Team),
    path('team/<int:member_id>', views.details, name='memberdetails')
]
