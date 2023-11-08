from django.db import router
from django.urls import path, include
from . import views

urlpatterns = [
    # path('list', views.index, name='list'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('', views.home, name='home'),

    # DRONE URLS
    path('drone_list', views.drone_list, name='drone_list'),
    path('drone_add', views.drone_add, name='drone_add'),
    path('drone_edit/<int:id>', views.drone_edit, name='drone_edit'),
    path('drone_update/<int:id>', views.drone_update, name='drone_update'),
    path('drone_delete/<int:id>', views.drone_delete, name='drone_delete'),

    # SWARM URLS
    path('swarm_list', views.swarm_list, name='swarm_list'),
    path('swarm_add', views.swarm_add, name='swarm_add'),
    path('swarm_edit/<int:id>', views.swarm_edit, name='swarm_edit'),
    path('swarm_update/<int:id>', views.swarm_update, name='swarm_update'),
    path('swarm_delete/<int:id>', views.swarm_delete, name='swarm_delete'),

    # USER URLS
    path('user_list', views.user_list, name='user_list'),
    path('user_add', views.user_add, name='user_add'),
    path('user_edit/<int:id>', views.user_edit, name='user_edit'),
    path('user_update/<int:id>', views.user_update, name='user_update'),
    path('user_delete/<int:id>', views.user_delete, name='user_delete'),

    # DJANGO REST PATHS
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]