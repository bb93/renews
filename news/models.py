from django.db import models

# Create your models here.
class Article(models.Model):
    url = models.CharField(max_length=200)
    crawled_date = models.DateTimeField('date crawled')
    title = models.CharField(max_length=200)
    body_text = models.TextField()