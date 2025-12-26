from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    age = models.IntegerField(null = True, blank = True)
    bio = models.TextField(blank = True)
    hobbies = models.CharField(max_length= 200, blank = True)
    
    def __str__(self):
        return self.name
    
    
    
   
class Student(models.Model):
    name = models.CharField( max_length=50, blank = False)
    address = models.TextField(max_length=900)
    email = models.EmailField(unique = True)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.name
       
       