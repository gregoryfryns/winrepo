from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def link_or_create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.filter(contact_email=instance.email).first()
        print('Instance: ' + instance.username)
        if profile is not None:
            # profile.user = instance
            instance.profile = profile
            instance.save()

        else:
            Profile.objects.create(user=instance,
                                   name=f'{instance.first_name} {instance.last_name}',
                                   contact_email=instance.email)
            print('created profile')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile is not None:
        instance.profile.save()
