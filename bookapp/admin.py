from django.contrib import admin

# Register your models here.
from bookapp import models

admin.site.register(models.User)
admin.site.register(models.Book)