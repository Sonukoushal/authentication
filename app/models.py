from django.db import models  # ⬅️ Ye sabse pehle hona chahiye

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
