from django.db import models


# in CoursePlanner directory
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)

