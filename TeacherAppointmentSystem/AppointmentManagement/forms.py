from django import forms
from AppointmentManagement.models import AppointmentInfo


class AppointmentForDayForm(forms.ModelForm):
    class Meta:
        model = AppointmentInfo
        fields = ['day','slot1_student_id','slot1_student_name', 'slot1_discussion_topic','slot2_student_id',
                  'slot2_student_name', 'slot2_discussion_topic','slot3_student_id','slot3_student_name',
                  'slot3_discussion_topic' ]


        labels = {
            'slot1_student_id' : 'Student ID',
            'slot1_student_name' : 'Student Name',
            'slot1_discussion_topic' : 'Discussion Topic',
            'slot2_student_id': 'Student ID',
            'slot2_student_name': 'Student Name',
            'slot2_discussion_topic': 'Discussion Topic',
            'slot3_student_id': 'Student ID',
            'slot3_student_name': 'Student Name',
            'slot3_discussion_topic': 'Discussion Topic',
            'slot4_student_id': 'Student ID',
            'slot4_student_name': 'Student Name',
            'slot4_discussion_topic': 'Discussion Topic',
            'slot5_student_id': 'Student ID',
            'slot5_student_name': 'Student Name',
            'slot5_discussion_topic': 'Discussion Topic',
            'slot6_student_id': 'Student ID',
            'slot6_student_name': 'Student Name',
            'slot6_discussion_topic': 'Discussion Topic',

        }


