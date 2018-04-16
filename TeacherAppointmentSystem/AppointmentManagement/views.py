from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import CreateView,View,UpdateView
from UserRegistration.models import User
from AppointmentManagement.forms import AppointmentForDayForm
from AppointmentManagement.models import AppointmentInfo
# Create your views here.


class ShowAppointments(View):
    def dispatch(self, request, *args, **kwargs, ):
        context = super(ShowAppointments, self).dispatch(request, *args, **kwargs)
        try:
           
        if request.user.is_authenticated and request.user.is_teacher:
           return render(request, 'AppointmentManagement/teacher_appointments.html', context)
        else:
           return render(request, 'UserRegistration/login_form.html')


class SetAppointment(CreateView):
    form_class = AppointmentForDayForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'UserRegistration/login_form.html')
        else:
            if request.user.is_teacher:
                form = self.form_class(None)
                return render(request,'AppointmentManagement/daily_apoointment_form.html', {'form': form})

            else:
                render(request, 'AppointmentManagement/daily_apoointment_form.html', {'form': form})


class UpdateAppointmentTime(UpdateView):
    model = AppointmentInfo
    form_class = AppointmentForDayForm
    template_name = 'AppointmentManagement/daily_apoointment_form.html'

    def get_success_url(self):
        user = AppointmentInfo.objects.get(pk= self.object.pk)
        return reverse('appointment_management:appointments', kwargs={'user_id':user.user_id})