from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.ProductAPI.as_view()),
    url(r'^(?P<id>[0-9]+)/$', views.ProductAPIWithId.as_view()),
]
