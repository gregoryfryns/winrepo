from django.contrib import admin

# Register your models here.
from .models import Profile, Recommandation

admin.site.register(Profile)
admin.site.register(Recommandation)