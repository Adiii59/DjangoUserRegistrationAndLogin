from django.contrib import admin

# Registering the "userProfile" model to store values in table.
from .models import userProfile
admin.site.register(userProfile) 

