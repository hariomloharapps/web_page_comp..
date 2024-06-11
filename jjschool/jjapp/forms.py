# from django import forms
# from .models import Teacher

# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ['username', 'password', 'name', 'email', 'class_teacher_of_grade', 'main_subject', 'extra_subjects']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }


from django import forms
from .models import CustomUser, Principal, Teacher, Student

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PrincipalForm(CustomUserForm):
    class Meta(CustomUserForm.Meta):
        fields = CustomUserForm.Meta.fields

class TeacherForm(CustomUserForm):
    class Meta(CustomUserForm.Meta):
        fields = CustomUserForm.Meta.fields + ['class_teacher_of_grade', 'main_subject', 'extra_subjects']

class StudentForm(CustomUserForm):
    class Meta(CustomUserForm.Meta):
        fields = CustomUserForm.Meta.fields + ['first_name', 'last_name', 'date_of_birth', 'admission_date', 'grade', 'performance', 'attendance_records', 'disciplinary_actions', 'total_fee', 'remaining_fee', 'attendance_percentage']
