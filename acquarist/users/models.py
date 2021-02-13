import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


def user_avatar_directory_path(instance, filename):
    file_name = f'avatar.{filename.split(".")[1]}'
    return 'users/{0}/{1}'.format(instance.id, file_name)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agree_to_terms = models.BooleanField(default=False)
    country = models.CharField(max_length=150, null=True, blank=True)
    region = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_directory_path, null=True, blank=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
