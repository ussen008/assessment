from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.forms import ControlForm, TeachingForm, PlanningForm, EducationalAchievmentsForm
from django.contrib.auth.decorators import login_required
from itertools import chain 

from myapp.models import ComprehensiveControl, Teaching, PlanningLesson, AssessmentStudentLearning
# Create your views here.

@login_required
def main(request):
    return render(request, 'myapp/index.html')
@login_required
def controlpage(request):
    if request.method == "POST":
        form = ControlForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваши данные успешно сохраннены')
            return redirect('myapp:main')
    else:
        form = ControlForm()
    return render(request, 'myapp/comprehensive_form.html', {'form': form})


def teachingform(request):
    if request.method =="POST":
        form = TeachingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваши данные успешно сохраннены')
            return redirect('myapp:main')
    else:
        form = TeachingForm()
    return render(request, 'myapp/teaching_form.html', {'form': form})

def planninglesson(request):
    if request.method == "POST":
        form = PlanningForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваши данные успешно сохраннены')
            return redirect('myapp:main')
    else:
        form = PlanningForm()
    return render(request, 'myapp/planning_form.html', {'form': form})


def educationachievment(request):
    if request.method == "POST":
        form = EducationalAchievmentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваши данные успешно сохраннены')
            return redirect('myapp:main')
    else:
        form = EducationalAchievmentsForm()
    return render(request, 'myapp/achievment.html', {'form': form})

@login_required
def assessment_for_me(request):
    forme = ComprehensiveControl.objects.filter(teacher=request.user)
    return render(request, 'myapp/for_me.html', {'forme': forme})

    
@login_required
def assessment_from_me(request):
    fromme = ComprehensiveControl.objects.filter(observer=request.user)
    
    return render(request, 'myapp/from_me.html', {'fromme': fromme})