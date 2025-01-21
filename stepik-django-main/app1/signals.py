from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Item)
def item_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New item created: {instance.name}")


def get_active_items():
    return Item.objects.active()


def get_books_by_author(author_id):
    return Book.objects.filter(author_id=author_id)


def get_recent_books(limit=5):
    return Book.objects.order_by('-publication_date')[:limit]


def get_books_with_price_range(min_price, max_price):
    return Book.objects.filter(price__gte=min_price, price__lte=max_price)