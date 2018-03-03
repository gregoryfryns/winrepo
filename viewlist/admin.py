from django.contrib import admin

# Register your models here.
from .models import Profile, Recommendation, Country

admin.site.register(Profile)
admin.site.register(Recommendation)
admin.site.register(Country)