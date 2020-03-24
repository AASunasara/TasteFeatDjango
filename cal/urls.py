from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.LoginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('factorylogs/', views.factorylogs, name='factorylogs'),
    path('show/', views.show, name='show'),
    path('factorylog_detail/', views.factorylog_detail, name='factorylog_detail'),
    path('delete_item/<list_id>', views.delete_item, name='delete_item'),
    path('delete_factorylog/<list_id>', views.delete_factorylog, name='delete_factorylog'),
    path('edit_item/<id>', views.edit_item, name='edit_item'),
    path('edit_factorylog/<id>', views.edit_factorylog, name='edit_factorylog'),
    # path('search/, views.search, name='search'),
    
]