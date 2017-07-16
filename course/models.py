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