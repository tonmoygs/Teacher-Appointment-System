from django.urls import path
from PersonalInfo.views import StudentProfileView,TeacherProfileView,FeedbackView,FeedbackList,FeedbackDetails,StudentUpdateView,\
    TeacherUpdateView,StudentInfoCreation,TeacherInfoCreation,StudentFeedbacks,ShowTeacherInfoToStudentView

app_name = 'personal_info'

urlpatterns = [
    path('student_profile/<int:pk>/', StudentProfileView.as_view(), name='student_profile'),
    path('teacher_profile/<int:pk>/', TeacherProfileView.as_view(), name='teacher_profile'),
    path('feedback_to_student/<int:pk>/', FeedbackView.as_view(), name='feedback_to_student'),
    path('feedback_list/<int:user_id>/', FeedbackList.as_view(), name='feedback_list'),
    path('feedback_list/feedback_details/<int:pk>/', FeedbackDetails.as_view(), name='feedback_details'),
    path('student_profile/<int:pk>/update/', StudentUpdateView.as_view(),name='student_update'),
    path('teacher_profile/<int:pk>/update/', TeacherUpdateView.as_view(),name='teacher_update'),
    path('student_info_creation/<int:pk>/', StudentInfoCreation.as_view(), name='student_info_creation'),


]
