from django.urls import path
from . import views
from .views import *
from django.urls import path




urlpatterns = [
    #--- user ---
    path("registers/", views.getRegisters),
    path("registers/create/", views.createRegister),
    path("registers/<str:pk>/update/", views.updateRegister),
    path("registers/<str:pk>/delete/", views.deleteRegister),
    path("registers/<str:pk>/", views.getRegister),
    #--- chat ---
    path("chat/", views.getchat),
    path("chat/create/", views.createchat),
    path("chat/<str:pk>/delete/", views.deleteChat),
    #--- food ---
    path("foods/", views.getFood1s),
    path("food/create1/", views.createFood1),
    path("food/<str:pk>/update/", views.updateFood1),
    path("food/<str:pk>/delete/", views.deleteFood1),
    path("food/<str:pk>/", views.getFood1),
    path("fooddate/<str:date>/", views.getFood1date),


]
