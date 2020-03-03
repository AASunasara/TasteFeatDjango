from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html',  redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('day/', views.day, name='day'),
    path('show/', views.show, name='show'),
    path('todays_detail/', views.todays_detail, name='todays_detail'),
    path('delete_item/<list_id>', views.delete_item, name='delete_item'),
    path('delete_day/<list_id>', views.delete_day, name='delete_day'),
    path('edit_item/<id>', views.edit_item, name='edit_item'),
    path('edit_day/<id>', views.edit_day, name='edit_day'),

]