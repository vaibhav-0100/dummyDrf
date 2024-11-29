from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'users', UserView, 'user')

urlpatterns = router.urls
