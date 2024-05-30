from django.urls import path
from .views import submit_application, success

urlpatterns = [
    path('apply/', submit_application, name='apply'),
    path('success/', success, name='success'),
]
