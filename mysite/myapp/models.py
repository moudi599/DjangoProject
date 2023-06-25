from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    publication_year = models.PositiveIntegerField()
    category = models.CharField(max_length=10)
