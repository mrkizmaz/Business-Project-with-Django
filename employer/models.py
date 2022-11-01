from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Employer(models.Model):
    username = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Username")
    position_int = models.CharField(max_length = 100, verbose_name = "Interested Position")
    skills = RichTextField()
    location = models.CharField(max_length = 50, verbose_name = "Location")
    resume = models.FileField(blank = True, null = True, verbose_name = "Add a resume (optional): ")

    def __str__(self):
        return self.username
