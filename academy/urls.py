from django.urls import path
from django.views.generic import TemplateView

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

    path('logins/', views.login_view, name='login'),
    path('master/', TemplateView.as_view(template_name='master_page.html'), name='master_page'),
    path('client/', TemplateView.as_view(template_name='client_page.html'), name='client_page'),
]
