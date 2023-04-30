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

