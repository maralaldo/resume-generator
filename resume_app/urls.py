from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_form_view, name='resume_form_view'),
    path('resume-preview/', views.resume_preview, name='resume_preview'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]
