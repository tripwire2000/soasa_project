from django.db import models

# Create your models here.
class Member(models.Model):
    name= models.CharField(max_length=200)
    photo= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(blank=True, max_length=200)
    email= models.EmailField(blank=True)
    phone= models.CharField(max_length=20, blank=True)
    is_current=models.BooleanField(default=False)
    def __str__(self):
        return self.name