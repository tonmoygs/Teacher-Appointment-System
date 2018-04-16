from django import forms
from RoutineManagement.models import RoutineInfo


class CreateRoutineForm(forms.ModelForm):
    class Meta:
        model = RoutineInfo
        fields = ['day','slot1_teacher_initial','slot1_course_name', 'slot1_course_code','slot1_room_no','slot1_section','slot2_teacher_initial',
                  'slot2_course_name', 'slot2_course_code','slot2_room_no','slot2_section','slot3_teacher_initial','slot3_course_name', 'slot3_course_code',
                  'slot3_room_no','slot3_section',]
        labels = {
            "slot1_teacher_initial" : "Teacher Initial",
            "slot1_course_name" : "Course Name",
            "slot1_course_code" : "Course Code",
            "slot1_room_no" : "Room No",
            "slot1_section" : "Section",
            "slot2_teacher_initial": "Teacher Initial",
            "slot2_course_name": "Course Name",
            "slot2_course_code": "Course Code",
            "slot2_room_no" : "Room No",
            "slot2_section": "Section",
            "slot3_teacher_initial": "Teacher Initial",
            "slot3_course_name": "Course Name",
            "slot3_course_code": "Course Code",
            "slot3_room_no": "Room No",
            "slot3_section": "Section",
            "slot4_teacher_initial": "Teacher Initial",
            "slot4_course_name": "Course Name",
            "slot4_course_code": "Course Code",
            "slot4_room_no": "Room No",
            "slot4_section": "Section",
            "slot5_teacher_initial": "Teacher Initial",
            "slot5_course_name": "Course Name",
            "slot5_course_code": "Course Code",
            "slot5_room_no": "Room No",
            "slot5_section": "Section",
            "slot6_teacher_initial": "Teacher Initial",
            "slot6_course_name": "Course Name",
            "slot6_course_code": "Course Code",
            "slot6_room_no": "Room No",
            "slot6_section": "Section"
        }


class CreateTeacherRoutineForm(forms.ModelForm):
    class Meta:
        model = RoutineInfo
        fields = ['day','slot1_course_name', 'slot1_course_code','slot1_room_no','slot1_section','slot2_course_name','slot2_course_code',
                  'slot2_room_no','slot2_section','slot3_course_name', 'slot3_course_code','slot3_room_no','slot3_section','slot4_course_name',
                  'slot4_course_code','slot4_room_no','slot4_section','slot5_course_name','slot5_course_code','slot5_room_no','slot5_section',
                  'slot6_course_name', 'slot6_course_code','slot6_room_no','slot6_section']
        labels = {
            "slot1_course_name" : "Course Name",
            "slot1_course_code" : "Course Code",
            "slot1_room_no" : "Room No",
            "slot1_section" : "Section",
            "slot2_course_name": "Course Name",
            "slot2_course_code": "Course Code",
            "slot2_room_no" : "Room No",
            "slot2_section": "Section",
            "slot3_course_name": "Course Name",
            "slot3_course_code": "Course Code",
            "slot3_room_no": "Room No",
            "slot3_section": "Section",
            "slot4_course_name": "Course Name",
            "slot4_course_code": "Course Code",
            "slot4_room_no": "Room No",
            "slot4_section": "Section",
            "slot5_course_name": "Course Name",
            "slot5_course_code": "Course Code",
            "slot5_room_no": "Room No",
            "slot5_section": "Section",
            "slot6_course_name": "Course Name",
            "slot6_course_code": "Course Code",
            "slot6_room_no": "Room No",
            "slot6_section": "Section",
        }