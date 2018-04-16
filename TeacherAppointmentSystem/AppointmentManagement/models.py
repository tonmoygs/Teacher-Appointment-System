from django.db import models
from UserRegistration.models import User
# Create your models here.


class AppointmentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    slot1_student_id = models.CharField(max_length=20, null=True, blank=True)
    slot1_student_name = models.CharField(max_length=50, null=True, blank=True)
    slot1_discussion_topic = models.CharField(max_length=100, null=True, blank=True)
    slot2_student_id = models.CharField(max_length=20, null=True, blank=True)
    slot2_student_name = models.CharField(max_length=50, null=True, blank=True)
    slot2_discussion_topic = models.CharField(max_length=100, null=True, blank=True)
    slot3_student_id = models.CharField(max_length=20, null=True, blank=True)
    slot3_student_name = models.CharField(max_length=50, null=True, blank=True)
    slot3_discussion_topic = models.CharField(max_length=100, null=True, blank=True)