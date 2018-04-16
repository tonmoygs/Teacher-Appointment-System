from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView, ListView,View,TemplateView
from django.core.mail import send_mail
from MailSending.forms import MailInfoForm
from UserRegistration.models import User
from MailSending.models import MailInfo
from RoutineManagement.models import RoutineInfo

# Create your views here.


class SendMailView(CreateView):
    form_class = MailInfoForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        if request.user.is_authenticated and request.user.is_student:

            return render(request, 'MailSending/student_mail_form.html', {'form':form,'teachers':initials})
        elif request.user.is_authenticated and request.user.is_student:
            return render(request, 'MailSending/teacher_mail_form.html', {'form': form})
        else:
            redirect('user_registration:user_login')

    def post(self, request, *args, **kwargs):

        user = get_object_or_404(User, pk = kwargs['pk'])
        form = self.form_class(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['mail_subject']
            sent_to = form.cleaned_data['sent_to']
            content_message = form.cleaned_data['mail_body']
            mail_from = user.user_mail
            mailinfo = form.save(commit=False)
            mailinfo.user = user
            send_mail(subject,content_message, mail_from, [sent_to], fail_silently=False)
            mailinfo.save()
            if request.user.is_authenticated and request.user.is_student:
                return redirect('mail_sending:mails', user.id)
            else:
                return redirect('mail_sending:teacher_mail_list', user.id)


class ShowMail(View):
    def dispatch(self, request, *args, **kwargs, ):
        context = super(ShowMail, self).dispatch(request, *args, **kwargs)
        context = {}
        try:
            context = {'mail': MailInfo.objects.filter(user_id=kwargs['user_id'])}
        except MailInfo.DoesNotExist:
            print("You have no mails.")
        try:
            context['routine'] = RoutineInfo.objects.filter(user_id=kwargs['user_id'])
            print(context['routine'])
            slot1 = context['routine'].values_list('slot1_teacher_initial')
            slot2 = context['routine'].values_list('slot2_teacher_initial')
            slot3 = context['routine'].values_list('slot3_teacher_initial')
            slot4 = context['routine'].values_list('slot4_teacher_initial')
            slot5 = context['routine'].values_list('slot5_teacher_initial')
            slot6 = context['routine'].values_list('slot6_teacher_initial')

            teacher_initial1 = list(slot1)
            teacher_initial2 = list(slot2)
            teacher_initial3 = list(slot3)
            teacher_initial4 = list(slot4)
            teacher_initial5 = list(slot5)
            teacher_initial6 = list(slot6)
            teacher_initials = teacher_initial1 + teacher_initial2 + teacher_initial3 + teacher_initial4 + teacher_initial5 + teacher_initial6
            initials = []
            for result in teacher_initials:
                result = filter(None, result)
                result = ''.join(result)
                if result != '':
                    initials.append(result)
            context['teachers'] = initials
        except RoutineInfo.DoesNotExist:
            print("You have no routine set yet")

        if request.user.is_authenticated and request.user.is_student:
            print(context)
        else:
            return render(request, 'UserRegistration/login_form.html')


class StudentMailListView(ListView):
    model = MailInfo
    template_name = 'MailSending/student_mail_list.html'
    context_object_name = 'mail'

    def get_queryset(self):
        return MailInfo.objects.all()


class TeacherMailListView(ListView):
    model = MailInfo
    template_name = 'MailSending/teacher_mail_list.html'
    context_object_name = 'mail'

    def get_queryset(self):
        return MailInfo.objects.all()


class Mail(TemplateView):
    template_name = 'MailSending/mail.html'
