from django.urls import path
from . import views

# Map url to views - custome defined functions that return HttpResponse
# given an HTTP request

urlpatterns = [
    path('about/', views.about, name = "about"), 
    #path('menu/', views.menu, name = "menu"),
    path('menu_card/', views.menu_by_id, name = "menu_card"),
    path('index/', views.index, name = "index"),
    path('', views.home, name = "home"),
    path('book/', views.form_view, name="book"),

]