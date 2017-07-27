from django.forms import ModelForm

from course.models import Student, Prof, Course, Question, Exam


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


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        exclude = ['questions', 'saved']