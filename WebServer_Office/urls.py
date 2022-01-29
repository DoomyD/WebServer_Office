from django.urls import path
from WebServer_Office import views
urlpatterns = [
    path('', views.main_page),
]