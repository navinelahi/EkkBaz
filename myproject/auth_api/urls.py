from django.urls import re_path as url
from auth_api import views

urlpatterns = [
    url(r'^api/register$', views.user_register),
    url(r'^api/login$', views.user_login),

]
