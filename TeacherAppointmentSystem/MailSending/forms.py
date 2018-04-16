from django import forms
from MailSending.models import MailInfo


class MailInfoForm(forms.ModelForm):
    class Meta:
        model = MailInfo
        fields = ['receivers_varsity_id','sent_to','mail_body']

        labels = {
            "receivers_varsity_id" : "Receiver's varsity ID",
            'mail_subject' : 'Subject',
            'sent_to' : 'TO',
            'mail_body' : 'Message'
        }