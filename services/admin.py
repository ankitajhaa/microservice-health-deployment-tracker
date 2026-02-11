from django.contrib import admin
from .models import Service, Environment

# Register your models here.
admin.site.register(Service)
admin.site.register(Environment)