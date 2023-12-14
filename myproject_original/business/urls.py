from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^api/register_business$', views.register_business),
    url(r'^api/nearby_business$', views.find_nearby_business),
    # url(r'^api/calculat$', views.user_login),

]