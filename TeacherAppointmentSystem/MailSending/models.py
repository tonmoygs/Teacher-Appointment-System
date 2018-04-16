from django.db import models
from UserRegistration.models import User
# Create your models here.


class MailInfo(models.Model):
    mail_subject = models.CharField(max_length=100, null=True, blank=True)
    sent_to = models.EmailField()
    mail_body = models.TextField()
    sent_time = models.TimeField(auto_now_add=True)
    sent_date = models.DateField(auto_now_add=True)
