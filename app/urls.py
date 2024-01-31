from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('videoCall/',views.videoCAll,name='videoCall'),
    path('logout/',views.user_logout,name='user_logout'),
    path('join_call/',views.join_call,name='join_call'),
    path('join_room/',views.join_room,name='join_room')
]
