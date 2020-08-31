from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.


class Resume(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    personal_profile = models.TextField()


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_detail = models.TextField()

class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Male'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('BE/Btech/BA/BSc/BCom', 'Masters'),
        ('12th', 'High School')
    )
    person = models.ForeignKey(Resume, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)

class Interest(models.Model):
    person = models.ForeignKey(Resume, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()

class Langauges(models.Model):
     person = models.ForeignKey(Resume, on_delete=models.CASCADE)
     Language=models.CharField(max_length=15)
    

