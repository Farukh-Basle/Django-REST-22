from django.urls import path,include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('users',views.UserViewSet)
routers.register('posts',views.PostViewSet)

urlpatterns = [
    path('',include(routers.urls)),
    path('posts/<int:pk>/comments/',
         views.PostViewSet.as_view({'get':'comments,','post':'comments'})),

]