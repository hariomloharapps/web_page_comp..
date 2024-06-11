from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='app1_register'),
    path('', views.user_login, name='principal_login'),
    # add more paths
]
