from django.db import models
from django.utils import timezone

# Multi Table Model
class Books(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class ISBN(models.Model):
    # Is generated automatically
    books_ptr = models.OneToOneField(
        Books, on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True)
    ISBN = models.TextField()
    detail = models.TextField(blank=True)

# Abstract Model
class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title']

class ItemA(BaseItem):
    content = models.TextField(max_length=255)

    class Meta(BaseItem.Meta):
        ordering = ['-created']

class ItemB(BaseItem):
    file = models.FileField(upload_to="images")