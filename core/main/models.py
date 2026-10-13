from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    skills = models.CharField(max_length=300)
    address = models.TextField()

    def __str__(self):
        return self.name
