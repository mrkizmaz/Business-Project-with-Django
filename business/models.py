from tabnanny import verbose
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

    class Meta:
        ordering = ['-published_date']

"""class Employers(models.Model):
    job = models.ForeignKey(Business, on_delete = models.CASCADE, verbose_name = "Business", related_name = "Applicants")
    emp_name = models.CharField(max_length = 50, verbose_name = "Name")
    skills = RichTextField()
    emp_resume = models.FileField(blank = True, null = True)
    applied_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.emp_name

    class Meta:
        ordering = ['-applied_date']"""

class Employers(models.Model):
    username = models.ForeignKey(Business, on_delete = models.CASCADE, verbose_name = "Username", related_name = "Applicants", blank=True, null = True)
    position_int = models.CharField(max_length = 100, verbose_name = "Interested Position", blank=True, null = True)
    skills = RichTextField()
    location = models.CharField(max_length = 50, verbose_name = "Location", blank=True, null = True)
    resume = models.FileField(blank = True, null = True, verbose_name = "Add a resume (optional): ")
    applied_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.emp_name

    class Meta:
        ordering = ['-applied_date']