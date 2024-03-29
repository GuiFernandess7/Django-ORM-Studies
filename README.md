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

To see the result, type ```python manage.py shell``` and the following command:

<img width="211" alt="Captura de tela 2023-04-29 162013" src="https://user-images.githubusercontent.com/63022500/235320576-cadcd986-c6d7-4281-8657-60c3f3d9538a.png">

### Custom Signal

Create a new file called signals.py and type:

```
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product

@receiver(post_save, sender=Product)
def example_receiver(sender, instance, created, **kwargs):
    print("Intance of Product is saved")
```

In the app.py:

```
from django.apps import AppConfig
from django.db.models.signals import post_save

def example_receiver(sender, **kwargs):
    print("Intance is saved")

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self) -> None:
        import myapp.signals
        
```

To see the parameters of a receiver, type the following in signals.py:

```
@receiver(post_save, sender=Product)
def example_receiver(sender, instance, created, **kwargs):
    print(instance)
    print(created)
    print("Intance of Product is saved")

```

and check:

```
>> from myapp.models import Product
>> Product(name="test").save()
Product object (4)
True
Intance of Product is saved
```

### ManyToManyProj

Django project about many to many relationship

models.py:

```
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField()
    category = models.ManyToManyField(Category, through="Product_Category")

    def __str__(self):
        return self.name

class Product_Category(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

```

The Product_Category class is the intermediate model table between Product and Category

To customize admin forms:

```
from django.contrib import admin
from .models import Category, Product, Product_Category

admin.site.register(Product_Category)

class CategoryInline(admin.TabularInline):
    model = Product.category.through

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }
    inlines = [CategoryInline]
```

### OR-query

Execute OR queries in views.py file:

```
from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)
    print(request)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})
```
