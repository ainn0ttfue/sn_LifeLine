from django.contrib import admin

# Register your models here.
from authapp.models import Person

admin.site.register(Person)
