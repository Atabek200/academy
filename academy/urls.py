from django.urls import path
from . import views
from .views import master_signup, client_signup, user_login

urlpatterns = [
    path('', views.main, name='home'),
    path('signup/master/', master_signup, name='master_signup'),
    path('signup/client/', client_signup, name='client_signup'),
    path('login/', user_login, name='login'),
]
