from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    query = models.TextField(max_length=150)
    date  = models.DateField(auto_now=True)
    def __str__(self):
        return self.name