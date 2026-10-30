import logging
from django.db.models.signals import post_delete
from django.dispatch import receiver
from apps.files.models import StoredFile
from apps.files.services import get_storage_service

logger = logging.getLogger(__name__)

@receiver(post_delete, sender=StoredFile)
def cleanup_storage_object_on_delete(sender, instance, **kwargs):
    """
    Automatically clean up object bytes from S3 when StoredFile is deleted.
    """
    if instance.object_key:
        try:
            storage = get_storage_service()
            storage.delete_object(instance.object_key)
            logger.info("Deleted underlying S3 object %s after file record %s was deleted.", instance.object_key, instance.id)
        except Exception as e:
            logger.warning("Failed deleting S3 object %s on file record deletion: %s", instance.object_key, e)
