from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from api.models import ExtendedUser, Profile

import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=ExtendedUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"Profile for user '{instance}' created")
