from django.contrib import admin

# Register your models here.
from ems_app import models

admin.site.register(models.User)
admin.site.register(models.Employee)
