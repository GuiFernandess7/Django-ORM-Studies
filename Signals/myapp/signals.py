from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product

@receiver(post_save, sender=Product)
def example_receiver(sender, instance, created, **kwargs):
    print("Intance of Product is saved")
