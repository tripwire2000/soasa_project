from django.db import models
from datetime import datetime

# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def snippet(self):
        return self.body[:50] + '...'