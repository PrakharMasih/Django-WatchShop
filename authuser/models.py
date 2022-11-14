
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='products/')

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()
    


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # phone = models.IntegerField()
    email = models.EmailField()
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def register(self):
        self.save()
