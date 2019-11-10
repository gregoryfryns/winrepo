from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


# @receiver(post_save, sender=Profile)
# def create_user(sender, instance, created, **kwargs):
#     print('Created ', created)
#     if created:
#         User.objects.create_user(**kwargs)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('Created ', created)
    if created:
        Profile.objects.create(user=instance,
                               name=f'{instance.first_name} {instance.last_name}',
                               contact_email=instance.email)
