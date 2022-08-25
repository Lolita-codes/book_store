from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=True)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} ({self.rating})'
