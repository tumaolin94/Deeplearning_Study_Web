from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    # post views
    url(r'^$', views.hello, name='hello'),
]