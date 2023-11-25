# from django.db import router
from django.urls import path, include
from . import views
from .views import (user_add, user_list, user_edit, user_delete, user_update, launch_swarm)
from .views import( drone_add, drone_list, drone_edit, drone_delete, drone_update)
from .views import( swarm_add, swarm_list, swarm_edit, swarm_delete, swarm_update)
from .views import( logout_view, login, index, register, home, control, connect, #launch,
                    ap_edit, ap_list, ap_add, ap_delete)

urlpatterns = [
    # path('list', views.index, name='list'),
    path('login', login, name='login'),
    path('index', index, name='index'),
    path('', home, name='home'),

    # DRONE URLS
    path('drone_list', drone_list, name='drone_list'),
    path('drone_add', drone_add, name='drone_add'),
    path('drone_edit/<int:id>', drone_edit, name='drone_edit'),
    path('drone_update/<int:id>', drone_update, name='drone_update'),
    path('drone_delete/<int:id>', drone_delete, name='drone_delete'),

    # SWARM URLS
    path('swarm_list', swarm_list, name='swarm_list'),
    path('swarm_add', swarm_add, name='swarm_add'),
    path('swarm_edit/<int:id>', swarm_edit, name='swarm_edit'),
    path('swarm_update/<int:id>', swarm_update, name='swarm_update'),
    path('swarm_delete/<int:id>', swarm_delete, name='swarm_delete'),

    # USER URLS
    path('user_list', user_list, name='user_list'),
    path('user_add', user_add, name='user_add'),
    path('user_edit/<int:id>', user_edit, name='user_edit'),
    path('user_update/<int:id>', user_update, name='user_update'),
    path('user_delete/<int:id>', user_delete, name='user_delete'),

    # OTHER URLS
    path('home', index, name='home'),
    path('control', control, name="control"),
    path('logout', logout_view, name='logout'),
    # path('registration', register, name="registration")

    # CONTROL URLS
    path('connect', connect, name='connect'),
    # path('launch', launch, name='launch'),
    path('launch_swarm/', launch_swarm, name='launch_swarm'),
    path('control/', control, name='control'),
    # path('tello_control/', control, name='tello_control'),



    # path('fly_drone', fly_drone, name='fly_drone')

    # ACCESS POINT URLS
    path('ap_list', ap_list, name='ap_list'),
    path('ap_edit/<int:id>', ap_edit, name='ap_edit'),
    path('ap_add>', ap_add, name='ap_add'),
    path('ap_delete/<int:id>', ap_delete, name='ap_delete'),


    # DJANGO REST PATHS
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]