from django.db import models
from django.utils import timezone

class Country(models.Model):
    code = models.CharField(max_length=2, blank=False, unique=True)
    name = models.CharField(max_length=60, blank=False)
    is_under_represented = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.code, self.name)

class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    webpage = models.URLField()
    institution = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    position = models.CharField(max_length=30, blank=False)
    grad_date = models.DateField()
    brain_structure = models.CharField(max_length=30)
    modalities = models.CharField(max_length=50)
    methods = models.CharField(max_length=50)
    domain = models.CharField(max_length=30)
    keywords = models.CharField(max_length=250)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ' - '.join([self.name, self.position, self.institution])

    def get_search_terms(self):
        return ' '.join([
            self.name, 
            self.institution, 
            self.country, 
            self.position, 
            self.brain_structure, 
            self.modalities,
            self.domain,
            self.keywords
        ])

class Recommendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_email = models.EmailField(blank=False)
    reviewer_position = models.CharField(max_length=30, blank=False)
    seen_at_conf = models.BooleanField()
    comment = models.CharField(max_length=500, blank=False)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s said '%s' to %s" % (self.reviewer_name, self.comment, self.profile.name)
