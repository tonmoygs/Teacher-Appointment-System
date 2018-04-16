from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import TemplateView, View,CreateView,UpdateView
from RoutineManagement.models import RoutineInfo
from UserRegistration.models import User
from RoutineManagement.forms import CreateRoutineForm,CreateTeacherRoutineForm
# Create your views here.


class ShowRoutine(View):
    def dispatch(self, request, *args, **kwargs, ):
        context = super(ShowRoutine, self).dispatch(request, *args, **kwargs)
        try:
            context = {'routine': RoutineInfo.objects.filter(user_id=kwargs['user_id'])}
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
                result = filter(None,result)
                result = ''.join(result)
                if result != '':
                    initials.append(result)
            print(initials)
            context['teachers'] = initials
        except RoutineInfo.DoesNotExist:
            print("You have no routine set yet")
        if request.user.is_authenticated and request.user.is_student:
            return render(request, 'RoutineManagement/studentRoutine.html', context)
        elif request.user.is_authenticated and request.user.is_teacher:
           return render(request, 'RoutineManagement/teacherRoutine.html', context)
        else:
           return render(request, 'UserRegistration/login_form.html')


class SetRoutine(CreateView):
    form_class = CreateRoutineForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'UserRegistration/login_form.html')
        else:
            try:
                context = {'routine': RoutineInfo.objects.filter(user_id=kwargs['pk'])}
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
                print(initials)

            except RoutineInfo.DoesNotExist:
                print("You have no routine set yet")

            if request.user.is_student:
                form = self.form_class(None)
                return render(request,'RoutineManagement/student_routine_form.html', {'form':form,'teachers':initials})
            else:
                if request.user.is_teacher:
                    form = self.form_class(None)
                    return render(request, 'RoutineManagement/teacher_routine_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'UserRegistration/login_form.html')
        else:
            user = get_object_or_404(User, pk=kwargs['pk'])
            form = self.form_class(request.POST)

            if form.is_valid():
                if request.user.is_student:
                    routinemanagement = form.save(commit=False)
                    routinemanagement.user = user
                    routinemanagement.save()
                    return redirect('routine_management:show_routine', user.id)


class TeacherRoutine(CreateView):
    form_class = CreateTeacherRoutineForm

    def get(self, request, *args, **kwargs):
    
                return render(request, 'RoutineManagement/teacher_routine_form.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'UserRegistration/login_form.html')
        else:
            user = get_object_or_404(User, pk=kwargs['pk'])
            form = self.form_class(request.POST)

            if form.is_valid():
                if request.user.is_teacher:
                    routinemanagement = form.save(commit=False)
                    routinemanagement.user = user
                    return redirect('routine_management:show_routine', user.id)
            else:
                return render(request, 'RoutineManagement/teacher_routine_form.html', {'form': form})


class UpdateTeacherRoutine(UpdateView):
    model = RoutineInfo
    form_class = CreateTeacherRoutineForm
    template_name = 'RoutineManagement/teacher_routine_form.html'

    def get_success_url(self):
        user = RoutineInfo.objects.get(pk= self.object.pk)
        