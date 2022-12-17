from django.urls import path
from . import views

# Map url to views - custome defined functions that return HttpResponse
# given an HTTP request

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('about/', views.about, name = "about"), 
    path('menu/', views.menu, name = "menu"),
    path('book/', views.book, name = "book"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
    #path('book/', views.form_view, name="book"),
    #path('index/', views.index, name = "index"),

]