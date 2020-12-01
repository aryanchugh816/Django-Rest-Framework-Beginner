from django.urls import path

from profiles_api import views


# Here we will map urls for our api
urlpatterns = [
    path('hellow-view/', views.HelloApiView.as_view())
]