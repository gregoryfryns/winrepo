from django.contrib import admin

# Register your models here.
from .models import Profile, Recommendation, Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_under_represented')
    
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'reviewer_name', 'reviewer_email', 'comment')
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'institution')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Country, CountryAdmin)