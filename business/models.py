from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Business(models.Model):
    publisher = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Publisher")
    company = models.CharField(max_length = 50, verbose_name = "The Company")
    position = models.CharField(max_length = 100, verbose_name = "Position")
    qualifications = RichTextField()
    location = models.CharField(max_length = 50, verbose_name = "Location")
    published_date = models.DateTimeField(auto_now_add = True, verbose_name = "Published Date")
    # job_image = models.ImageField(blank = True, null = True, verbose_name = "Add a picture (optional): ")

    def __str__(self):
        return self.position


