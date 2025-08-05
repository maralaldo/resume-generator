from django.urls import path
from .views import resume_form_view

urlpatterns = [
    path('', resume_form_view, name='resume-form'),
]
