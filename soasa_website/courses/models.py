from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=300)
    course_code=models.CharField(max_length=100)
    level = models.CharField(max_length=5)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    def __str__(self):
        return self.name