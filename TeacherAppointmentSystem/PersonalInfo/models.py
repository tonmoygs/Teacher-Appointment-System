from django.urls import reverse
from django.db import models
from UserRegistration.models import User
# Create your models here.


class StudentInfo(Person):
    student_sec = models.CharField(max_length=2)
    student_dept = models.CharField(max_length=5)


class TeacherInfo(Person):
    teacher_initial = models.CharField(max_length=10)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=30)
    feedback_body = models.TextField()
    feedback_DateTime = models.DateTimeField(auto_now_add=True)

