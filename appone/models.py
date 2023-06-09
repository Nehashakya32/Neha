from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30,null=True)
    dob=models.DateField(auto_created=True, null=True)
    address=models.TextField(null=True)
    grade=models.CharField(max_length=5,null=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    phone=models.IntegerField(null=True)
    department=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Signup(models.Model):
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30,null=True)
    username=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=30,null=True)
    
