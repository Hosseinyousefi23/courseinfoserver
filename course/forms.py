from django.forms import ModelForm

from course.models import Student, Prof, Course


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'