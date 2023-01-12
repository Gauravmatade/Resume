from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Email = models.EmailField()
    ContactNo = models.CharField(max_length = 100)
    Gender = models.CharField(max_length = 100)
    DOB = models.DateField()
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Programming_Language = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
    Prefered_loc = models.CharField(max_length=100)
    Prof_image = models.ImageField(upload_to="Profile_Images/",blank=True)
    Project = models.TextField()

