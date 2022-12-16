from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1>')

def index(request):
    return HttpResponse('<h2> These are my projects: </h2>')

def form_view(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)

# Create view to render html template
# update url patterns at project and app levels#
def about(request):
    # dictionary with content to render dynamically
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    # pass dictionary to render 
    return render(request, "about.html", {"content": about_content})

def menu(request):
    menu_content = {'menu': "Various menu items - content goes here"} 
    return render(request, "menu.html", {'content': menu_content})