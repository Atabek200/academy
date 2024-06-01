from django.urls import path
from . import views
from .views import master_signup, client_signup

urlpatterns = [
    path('', views.main, name='home'),
    path('index/', views.index, name='index'),
    path('signup/master/', master_signup, name='master_signup'),
    path('signup/client/', client_signup, name='client_signup'),

    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('create/', views.ticket_create, name='ticket_create'),
    path('<int:pk>/update/', views.ticket_update, name='ticket_update'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
