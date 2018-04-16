from django.urls import path
from MailSending.views import SendMailView, StudentMailListView,TeacherMailListView,ShowMail,Mail

app_name = 'mail_sending'

urlpatterns = [
    path('send_mail/<int:pk>/', SendMailView.as_view(), name='send_mail'),
    path('mails/<int:user_id>/', ShowMail.as_view(), name='mails'),
    path('mail_sending/', Mail.as_view(), name="mail")
]