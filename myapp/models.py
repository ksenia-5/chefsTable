from django.db import models
from unicodedata import name

# Create your models here.
class DrinkCategory(models.Model):
    category_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.category_name


class Drink(models.Model):
    drink = models.CharField(max_length = 200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinkCategory, on_delete = models.PROTECT, default = None)
    
    def __str__(self):
        return self.drink

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now = True)
    comments = models.CharField(max_length= 1000)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    role = models.CharField(max_length = 100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name