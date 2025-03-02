from django.db import models

class Course(models.Model):
    Course_id = models.CharField(max_length=128)
    Course_name = models.CharField(max_length=128)
    Teacher_name = models.CharField(max_length=128)
