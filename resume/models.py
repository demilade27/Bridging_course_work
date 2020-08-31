from django.utils import timezone
from django.db import models
from django.conf import settings
import datetime


# Create your models here.
class Resume(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    personal_profile = models.TextField()

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    job = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    position =models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year =models.CharField(max_length=4)
    description =models.TextField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    level=models.CharField(max_length=50)   
    degree = models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=4)
    end_year =models.CharField(max_length=4)
    result = models.CharField(max_length=54)


class ProfessionalSkills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    skill = models.CharField(max_length=60)



class Interest(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
    intrest = models.TextField()

class Langauges(models.Model):
     resume = models.ForeignKey(Resume, on_delete=models.CASCADE,null=True)
     Language=models.CharField(max_length=15)

    

