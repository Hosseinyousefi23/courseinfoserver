from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=100)
    national_code = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Prof(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    prof = models.ForeignKey(Prof, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name


class Question(models.Model):
    question_face = models.CharField(max_length=300)
    first_choice = models.CharField(max_length=50)
    second_choice = models.CharField(max_length=50)
    third_choice = models.CharField(max_length=50)
    fourth_choice = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    course = models.ForeignKey(Course, related_name='questions')


class Exam(models.Model):
    course = models.ForeignKey(Course, related_name='exams')
    diff1count = models.IntegerField()
    diff2count = models.IntegerField()
    diff3count = models.IntegerField()
    diff4count = models.IntegerField()
    diff5count = models.IntegerField()
    questions = models.ManyToManyField(Question, related_name='exams')
    saved = models.BooleanField(default=False)
