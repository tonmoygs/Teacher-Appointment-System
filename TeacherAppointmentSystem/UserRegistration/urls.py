from django.urls import path
from UserRegistration.views import StudentSignup,TeacherSignup,UserLoginView,TeacherOrStudent
from django.contrib.auth import views as auth_views

app_name = 'user_registration'

urlpatterns = [
    path('accounts/student_signup/', StudentSignup.as_view(), name='student_signup'),
    path('accounts/teacher_signup/', TeacherSignup.as_view(), name='teacher_signup'),
    path('accounts/login/', UserLoginView.as_view(), name='user_login'),
    path('accounts/logout/', auth_views.logout,{'next_page':'user_registration:user_login'}, name='user_logout'),
    path('teacher_or_student/', TeacherOrStudent.as_view(), name='teacher_or_student')

]
