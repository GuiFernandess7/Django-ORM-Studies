![django-orm](https://user-images.githubusercontent.com/63022500/235320076-f0400f8c-1dae-4740-89da-bbcbee89fc43.jpg)

# Django ORM Studies
Django ORM Studies

### Signals

(PT: Signals permitem que uma mensagem seja exibida após uma mudança ocorrer na tabela do banco de dados)

Basic app with signals implemented

Step 1:

Add a model. Example:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
```

Add a signal in the apps.py:

```
from django.apps import AppConfig
from django.db.models.signals import post_save

def example_receiver(sender, **kwargs):
    print("Intance is saved")

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self) -> None:
        post_save.connect(example_receiver)

```
