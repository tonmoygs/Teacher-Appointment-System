from django import forms
from PersonalInfo.models import Feedback,Person


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student_id', 'feedback_body']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Person
