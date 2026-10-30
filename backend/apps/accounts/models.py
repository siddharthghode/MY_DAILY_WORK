import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    tenant_id = models.CharField(max_length=64, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.tenant_id and self.user_id:
            self.tenant_id = f"tenant_{self.user_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.tenant_id})"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, tenant_id=f"tenant_{instance.id}")
