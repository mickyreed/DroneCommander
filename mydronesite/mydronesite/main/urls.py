from django.urls import path
from . import views

urlpatterns = [
    # path('list', views.index, name='list'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('add_drone', views.add_drone, name='add_drone'),
    path('add_swarm', views.add_swarm, name='add_swarm'),
    path('user_list', views.user_list, name='user_list'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user', views.update_user, name='update_user'),
    path('', views.home, name='home'),
]