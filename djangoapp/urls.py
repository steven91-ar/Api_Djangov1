from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.getUsers),
    path('create', views.addUser),
    path('read/<str:ss>', views.getUser),
    path('update/<str:ss>', views.updateUser),
    path('delete/<str:ss>', views.deleteUser),
]

