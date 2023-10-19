from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name',max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Car(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Car name', max_length=60)
    img = models.ImageField('Car image', upload_to='images')
    price = models.PositiveIntegerField('Car price')

    def __str__(self):
        return self.name