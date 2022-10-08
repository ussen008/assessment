from dataclasses import field, fields
from django import forms
from .models import *

class ControlForm(forms.ModelForm):
    class Meta:
        model = ComprehensiveControl
        fields = '__all__'


class TeachingForm(forms.ModelForm):
    class Meta:
        model = Teaching
        fields = '__all__'


class PlanningForm(forms.ModelForm):
    class Meta:
        model = PlanningLesson
        fields = '__all__'


class EducationalAchievmentsForm(forms.ModelForm):
    class Meta:
        model = AssessmentStudentLearning
        fields = '__all__'