from django.urls import path
from . import views

# Map url to views - custome defined functions that return HttpResponse
# given an HTTP request

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('', views.home, name = "home"),
    path('shift/', views.form_view, name="shift"),

]