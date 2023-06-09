from django.urls import path,include
from rest_framework.routers import DefaultRouter
from appone.api import views

router=DefaultRouter()
router.register('',views.StudentViewSet,basename="student")

routers=DefaultRouter()
routers.register('',views.TeacherViewSet,basename="teacher")

urlpatterns=[
    path('student/',include(router.urls)),
    path('teacher/',include(routers.urls)),
]