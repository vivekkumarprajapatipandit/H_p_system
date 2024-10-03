from django.db import models

class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Username  = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Language = models.CharField(max_length=50)
    Aadhar = models.IntegerField()
    Profilepic = models.ImageField(upload_to='profile_pics',blank=True)  
 

 
