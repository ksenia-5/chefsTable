from django.contrib import admin
from .models import Drink, DrinkCategory, Booking, Employee

# Register your models here.
admin.site.register(Drink)
admin.site.register(DrinkCategory)
admin.site.register(Booking)
admin.site.register(Employee)

