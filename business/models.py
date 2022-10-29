from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Business(models.Model):
    publisher = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Publisher")
    company = models.CharField(max_length = 50, verbose_name = "The Company")
    position = models.CharField(max_length = 50, verbose_name = "Position")
    qualifications = models.TextField(verbose_name = "Qualifications")
    location = models.CharField(max_length = 50, verbose_name = "Location")
    published_date = models.DateTimeField(auto_now_add = True, verbose_name = "Published Date")

    def __str__(self):
        return self.position

