from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2089, blank=True)
    follow_author = models.CharField(max_length=2089, blank=True)
    book_available = models.BooleanField()

    def __str__(self):
        return self.title


