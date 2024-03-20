from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_profile_list, name='user_profile_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('staff/', views.items_list, name='staff'),
    path('logout/', views.log_out, name='logout'),
]
