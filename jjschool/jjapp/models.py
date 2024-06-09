from django.db import models

class Principal(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed


from django.contrib.auth.hashers import make_password

def create_principal():
    Principal.objects.create(
        username='principal_username',
        password=make_password('principal_password'),
        # Set other field values
    )

from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    admission_date = models.DateField()
    grade = models.CharField(max_length=10)
    performance = models.TextField()
    attendance_records = models.TextField()
    disciplinary_actions = models.TextField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    attendance_percentage = models.FloatField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models

class Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    class_teacher_of_grade = models.CharField(max_length=10)  # New field
    main_subject = models.CharField(max_length=100)  # New field
    extra_subjects = models.CharField(max_length=200, blank=True, null=True)  # New field, optional

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming teacher is a user

    class Meta:
        unique_together = ('student', 'date')

