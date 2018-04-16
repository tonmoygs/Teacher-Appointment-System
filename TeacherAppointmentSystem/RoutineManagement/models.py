from django.db import models
from UserRegistration.models import User

# Create your models here.


class RoutineInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    slot1_teacher_initial = models.CharField(max_length=5, null=True, blank=True)
    slot1_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot1_course_code = models.CharField(max_length=10, null=True,blank=True)
    slot1_room_no = models.IntegerField(null=True,blank=True)
    slot1_section = models.CharField(max_length=5,null=True,blank=True)

    slot2_teacher_initial = models.CharField(max_length=5, null=True, blank=True)
    slot2_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot2_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot2_room_no = models.IntegerField(null=True, blank=True)
    slot2_section = models.CharField(max_length=5,null=True, blank=True)

    slot3_teacher_initial = models.CharField(max_length=5, null=True, blank=True)
    slot3_course_name = models.CharField(max_length=100, null=True, blank=True)
    slot3_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot3_room_no = models.IntegerField(null=True, blank=True)
    slot3_section = models.CharField(max_length=5,null=True, blank=True)



class TeacherRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    slot1_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot1_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot1_course_code = models.CharField(max_length=10, null=True,blank=True)
    slot2_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot2_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot2_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot3_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot3_course_name = models.CharField(max_length=100, null=True, blank=True)
    slot3_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot4_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot4_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot4_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot5_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot5_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot5_course_code = models.CharField(max_length=10, null=True, blank=True)
    slot6_room_no = models.CharField(max_length=5, null=True, blank=True)
    slot6_course_name = models.CharField(max_length=100, null=True,blank=True)
    slot6_course_code = models.CharField(max_length=10, null=True, blank=True)