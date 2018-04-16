from django.urls import path
from RoutineManagement.views import ShowRoutine, SetRoutine,TeacherRoutine,UpdateTeacherRoutine

app_name = 'routine_management'

urlpatterns = [
    path('show_routine/<int:user_id>/', ShowRoutine.as_view(), name='show_routine'),
    path('update_teacher_routine/<int:pk>/', UpdateTeacherRoutine.as_view(), name='update_teacher_routine')
]