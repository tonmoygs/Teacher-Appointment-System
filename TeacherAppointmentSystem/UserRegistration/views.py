from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView,View,TemplateView

from UserRegistration.models import User
from UserRegistration.forms import StudentSignupForm,TeacherSignupForm, UserLoginForm

# Create your views here.


class StudentSignup(CreateView):
    model = User
    form_class = StudentSignupForm
    template_name = 'UserRegistration/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)


class TeacherSignup(CreateView):
    model = User
    form_class = TeacherSignupForm
    template_name = 'UserRegistration/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('personal_info:teacher_profile', user.id)


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'UserRegistration/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
            if user is not None:
                login(request, user)
                if request.user.is_student:
                    return redirect('routine_management:show_routine', user.id)
                elif request.user.is_teacher:
                    return redirect('routine_management:show_routine', user.id)
        return render(request, self.template_name, {'form': form})


class TeacherOrStudent(TemplateView):
    template_name = 'UserRegistration/select_teacher_student.html'
