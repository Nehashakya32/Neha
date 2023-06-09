
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login',views.Login,name='login'),
    path('home',views.home,name='home'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('updatestudent/<int:pk>',views.updatestudent,name='updatestudent'),
    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),
    path('teacher',views.teacher,name='teacher'),
    path('addteacher',views.addteacher,name='addteacher'),
    path('updateteacher/<int:pk>',views.updateteacher,name='updateteacher'),
    path('deleteteacher/<int:pk>',views.deleteteacher,name='deleteteacher'),
    path('Logout',views.Logout,name='Logout'),
    path('api/',include('appone.api.urls')),
]
