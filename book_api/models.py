from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title
