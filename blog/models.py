from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')
