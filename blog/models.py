from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')

    def summary(self):
        return self.body[:100]

    def date_time(self):
        return self.publish_date.strftime('%d %B, %Y')

    def __str__(self):
        #editing title for admin panel
        return self.title
