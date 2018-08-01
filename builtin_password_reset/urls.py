from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views

from_email = settings.DEFAULT_FROM_EMAIL

urlpatterns = [
    url(r'^reset_password/$', views.password_reset, {'from_email': from_email }, name='reset_password'),
    url(r'^reset_password/submitted/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/complete/$', views.password_reset_complete, name='password_reset_complete'),
]
