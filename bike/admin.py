from django.contrib import admin
from .models import Bike

# Register your models here.
admin.site.register(Bike)


def __str__(self):
      return self.name