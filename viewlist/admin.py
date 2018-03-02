from django.contrib import admin

# Register your models here.
from .models import Profile, Recommendation

admin.site.register(Profile)
admin.site.register(Recommendation)