from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)
    webpage = models.URLField()
    institution = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=70, blank=False)
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

class Recommendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_email = models.EmailField(blank=False)
    reviewer_position = models.CharField(max_length=30, blank=False)
    seen_at_conf = models.BooleanField()
    comment = models.CharField(max_length=500)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s said '%s' to %s" % (self.reviewer_name, self.comment, self.profile.name)