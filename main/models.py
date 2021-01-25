from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
