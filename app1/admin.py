from django.contrib import admin

from .models import *

# Register your models here.
print('in admin.py-------------')

admin.site.register([Book, College])