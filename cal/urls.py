from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html',  redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('day/', views.day, name='day'),
    path('show/', views.show, name='show'),
]