from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Lượt truy cập: {self.count}"