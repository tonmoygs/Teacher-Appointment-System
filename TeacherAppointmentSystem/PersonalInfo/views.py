from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import TemplateView,View,CreateView,ListView,DetailView,UpdateView
from PersonalInfo.forms import FeedbackForm,StudentForm,TeacherForm
from UserRegistration.models import User
from PersonalInfo.models import Feedback, Person


class StudentProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        context = super(StudentProfileView, self).dispatch(request, *args, **kwargs)
        context = {}
        try:
            context = {'person': Person.objects.get(user_id=kwargs['pk'])}
        except Person.DoesNotExist:
            print("You have no info set yet")
        context['person_initialinfo'] = User.objects.get(pk=kwargs['pk'])
        return render(request, 'PersonalInfo/student_profile.html', context)


class TeacherProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        context = super(TeacherProfileView, self).dispatch(request, *args, **kwargs)
        context = {}
        try:
            context = {'person': Person.objects.get(user_id=kwargs['pk'])}
        except Person.DoesNotExist
        return render(request, 'PersonalInfo/teacher_profile.html', context)


class StudentInfoCreation(CreateView):
    form_class = StudentForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_student:
            return render(request, 'UserRegistration/login_form.html')
        else:
            form = self.form_class(None)
            return render(request,'PersonalInfo/student_update_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('personal_info:student_profile', user.id)
        else:
            return render(request,'PersonalInfo/student_update_form.html',{'form':form})


class TeacherInfoCreation(CreateView):
    form_class = TeacherForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_teacher:
            return render(request, 'UserRegistration/login_form.html')
        else:
            form = self.form_class(None)
            return render(request, 'PersonalInfo/teacher_update_form.html', {'form': form})

    def post(self, request, *args, **kwargs):

        if form.is_valid():
            person = form.save(commit=False)
            person.user = user
            person.save()
            return redirect('personal_info:teacher_profile', user.id)
        else:
            return render(request, 'PersonalInfo/student_update_form.html', {'form': form})


class StudentUpdateView(UpdateView):
    model = Person
    form_class = StudentForm
    template_name = 'PersonalInfo/student_update_form.html'

    def get_success_url(self):
        user = Person.objects.get(pk=self.object.pk)
        return reverse('personal_info:student_profile', kwargs={'pk':user.user_id})


class TeacherUpdateView(UpdateView):
    model = Person
    form_class = TeacherForm
    template_name = 'PersonalInfo/teacher_update_form.html'

    def get_success_url(self):
        user = Person.objects.get(pk= self.object.pk)
        return reverse('personal_info:teacher_profile', kwargs={'pk':user.user_id})


class FeedbackView(CreateView):
    form_class = FeedbackForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_teacher:
            return render(request, 'UserRegistration/login_form.html')
        else:
            form = self.form_class(None)
            return render(request, 'PersonalInfo/feedback_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.is_teacher:
            return render(request, 'UserRegistration/login_form.html')
        else:
            user = get_object_or_404(User, pk = kwargs['pk'])
            form = self.form_class(request.POST)

                return redirect('personal_info:feedback_list', user.id)
            else:
                return render(request, 'PersonalInfo/feedback_form.html', {'form': form})


class FeedbackList(ListView):
    model = Feedback
    template_name = 'PersonalInfo/feedback_list.html'
    context_object_name = 'feedback'

    def get_queryset(self):
        return Feedback.objects.all()


class FeedbackDetails(DetailView):
    model = Feedback
    template_name = 'PersonalInfo/feedback_details.html'


class StudentFeedbacks(ListView):
    model = Feedback
    template_name = 'PersonalInfo/student_feedbacks.html'
    context_object_name = 'student_feedbacks'

    def get_queryset(self,**kwargs):
        return Feedback.objects.filter(student_id = self.kwargs['varsity_id'])


class ShowTeacherInfoToStudentView(View):
    def dispatch(self, request, *args, **kwargs):
        context = super(ShowTeacherInfoToStudentView, self).dispatch(request, *args, **kwargs)
        context = {}
        try:
            teacher = User.objects.get(teacher_initial=kwargs['teacher_initial'])
        except Person.DoesNotExist:

        return render(request, 'PersonalInfo/show_teacher_info_to_student.html', {'teacher':teacher, 'person':person})