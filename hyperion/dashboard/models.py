from django.db import models

# Create your models here.
class Graph(models.Model):
    name = models.CharField(max_length=256)
    query = models.TextField()
