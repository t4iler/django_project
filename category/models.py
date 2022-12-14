from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    slug = models.SlugField(max_length=70, primary_key=True)
    name = models.CharField(max_length=60, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'