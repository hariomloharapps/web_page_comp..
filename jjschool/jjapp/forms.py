from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['username', 'password', 'name', 'email', 'class_teacher_of_grade', 'main_subject', 'extra_subjects']
        widgets = {
            'password': forms.PasswordInput(),
        }
