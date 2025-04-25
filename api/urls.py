from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet
from django.urls import path, re_path
from django.views.generic import TemplateView
from fastapi import FastAPI

# Add FastAPI app instance
app = FastAPI()

urlpatterns = [
    path("registers/", views.getRegisters),
    path("registers/create/", views.createRegister),
    path("registers/<str:pk>/update/", views.updateRegister),
    path("registers/<str:pk>/delete/", views.deleteRegister),
    path("registers/<str:pk>/", views.getRegister),
    # path("upload/", upload_image, name="upload_image"),
    path('ph/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
]

urlpatterns += [
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
    # path("upload-image/", views.upload_image, name="upload_image"),
    path("get-image/<str:filename>/", views.get_image, name="get_image"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)