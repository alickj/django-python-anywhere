from django.urls import path
from basic_app import views


# Template tagging
# https://docs.djangoproject.com/en/3.1/ref/urls/
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]