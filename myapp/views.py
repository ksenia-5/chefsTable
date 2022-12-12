from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1>')

def index(request):
    return HttpResponse('<h2> These are my projects: </h2>')

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "shift.html", context)