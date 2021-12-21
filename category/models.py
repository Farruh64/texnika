from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    description = models.TextField(blank = True)
    image = models.ImageField(blank = True) 
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_url(self):
        return reverse('products_by_category', args = [self.slug])     
# Create your models here.
