from django.urls import path
from .views import submit_application, success, confirm_application

urlpatterns = [
    path('apply/', submit_application, name='apply'),
    path('success/', success, name='success'),
    path('confirm_application/<int:application_id>/', confirm_application, name='confirm_application'),
]
