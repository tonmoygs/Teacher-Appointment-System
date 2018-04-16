from django.urls import path
from AppointmentManagement.views import SetAppointment,ShowAppointments,UpdateAppointmentTime

app_name = 'appointment_management'

urlpatterns = [
    path('appointments/<int:user_id>/', ShowAppointments.as_view(), name='appointments'),
    path('set_appointment/<int:pk>/', SetAppointment.as_view(), name='set_appointment'),
    path('update_appointment/<int:pk>/', UpdateAppointmentTime.as_view(), name='update_appointment')
]
