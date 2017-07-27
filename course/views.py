import random

from django.core.serializers import serialize
from django.db.models.expressions import Value
from django.db.models.functions.base import Concat
from django.http.response import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls.base import reverse

from course.forms import StudentForm, ProfForm, CourseForm, QuestionForm, ExamForm
from course.models import Student, Prof, Course, Question, Exam


def main_page(request):
    return render(request, "main_page.html",
                  {'student_count': Student.objects.all().count(), 'prof_count': Prof.objects.all().count(),
                   'course_count': Course.objects.all().count(),
                   'question_count': Question.objects.all().count(),
                   'exam_count': Exam.objects.filter(saved=True).count()})


def students(request):
    return render(request, "students.html", {'students': Student.objects.all})


def add_student(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request, 'add_student.html', {'form': form})
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('course:students'))


def edit_student(request):
    if request.method == 'GET':
        if 'id' in request.GET and Student.objects.filter(id=request.GET['id']).count() > 0:
            student = Student.objects.get(id=request.GET['id'])
            form = StudentForm(instance=student)
            return render(request, 'edit_student.html', {'id': request.GET['id'], 'form': form})
        else:
            return render(request, 'not_found.html', {})
    elif request.method == 'POST':
        sid = request.POST['student_id']
        student = Student.objects.get(id=sid)
        form = StudentForm(request.POST, instance=student)
        form.save()
        return HttpResponseRedirect(reverse('course:students'))


def delete_student(request):
    student = Student.objects.get(id=request.GET['id'])
    student.delete()
    return HttpResponseRedirect(reverse('course:students'))


def profs(request):
    return render(request, 'profs.html', {'profs': Prof.objects.all})


def add_prof(request):
    if request.method == 'GET':
        form = ProfForm()
        return render(request, 'add_prof.html', {'form': form})
    elif request.method == 'POST':
        form = ProfForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('course:profs'))


def edit_prof(request):
    if request.method == 'GET':
        if 'id' in request.GET and Prof.objects.filter(id=request.GET['id']).count() > 0:
            prof = Prof.objects.get(id=request.GET['id'])
            form = ProfForm(instance=prof)
            return render(request, 'edit_prof.html', {'id': request.GET['id'], 'form': form})
        else:
            return render(request, 'not_found.html', {})
    elif request.method == 'POST':
        pid = request.POST['prof_id']
        prof = Prof.objects.get(id=pid)
        form = ProfForm(request.POST, instance=prof)
        form.save()
        return HttpResponseRedirect(reverse('course:profs'))


def delete_prof(request):
    prof = Prof.objects.get(id=request.GET['id'])
    prof.delete()
    return HttpResponseRedirect(reverse('course:profs'))


def courses(request):
    return render(request, 'courses.html', {'courses': Course.objects.all})


def add_course(request):
    if request.method == 'GET':
        form = CourseForm()
        return render(request, 'add_course.html', {'form': form})
    elif request.method == 'POST':
        form = CourseForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('course:courses'))


def edit_course(request):
    if request.method == 'GET':
        if 'id' in request.GET and Course.objects.filter(id=request.GET['id']).count() > 0:
            course = Course.objects.get(id=request.GET['id'])
            form = CourseForm(instance=course)
            return render(request, 'edit_course.html', {'id': request.GET['id'], 'form': form})
        else:
            return render(request, 'not_found.html', {})
    elif request.method == 'POST':
        cid = request.POST['course_id']
        course = Course.objects.get(id=cid)
        form = CourseForm(request.POST, instance=course)
        form.save()
        return HttpResponseRedirect(reverse('course:courses'))


def delete_course(request):
    course = Course.objects.get(id=request.GET['id'])
    course.delete()
    return HttpResponseRedirect(reverse('course:courses'))


def search(request):
    if 'course' in request.GET:
        courses = Course.objects.filter(name__contains=request.GET['course'])
        return JsonResponse({'courses': serialize('json', courses)})
    elif 'prof' in request.GET:
        profs = Prof.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name')).filter(
            full_name__contains=request.GET['prof'])
        return JsonResponse({'profs': serialize('json', profs)})
    elif 'student' in request.GET:
        students = Student.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name')).filter(
            full_name__contains=request.GET['student'])
        return JsonResponse({'students': serialize('json', students)})
    else:
        return Http404('not found')


def questions(request):
    questions = Question.objects.all()
    all_course = Course.objects.all()
    return render(request, 'questions.html', {'courses': all_course, 'questions': questions})


def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'add_question.html', {'form': form})
    elif request.method == 'POST':
        form = QuestionForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('course:questions'))


def edit_question(request):
    if request.method == 'GET':
        if 'id' in request.GET and Question.objects.filter(id=request.GET['id']).count() > 0:
            question = Question.objects.get(id=request.GET['id'])
            form = QuestionForm(instance=question)
            return render(request, 'edit_question.html', {'id': request.GET['id'], 'form': form})
        else:
            return render(request, 'not_found.html', {})
    elif request.method == 'POST':
        qid = request.POST['question_id']
        question = Question.objects.get(id=qid)
        form = QuestionForm(request.POST, instance=question)
        form.save()
        return HttpResponseRedirect(reverse('course:questions'))


def delete_question(request):
    question = Question.objects.get(id=request.GET['id'])
    question.delete()
    return HttpResponseRedirect(reverse('course:questions'))


def exams(request):
    exams = Exam.objects.filter(saved=True)
    all_course = Course.objects.all()
    return render(request, 'exams.html', {'courses': all_course, 'exams': exams})


def add_exam(request):
    if request.method == 'GET':
        form = ExamForm()
        return render(request, 'add_exam.html', {'form': form})
    elif request.method == 'POST':
        form = ExamForm(request.POST)
        exam = form.save()
        diff1 = Question.objects.filter(difficulty=1).values_list('id', flat=True)
        rand_diff1 = random.sample(list(diff1), exam.diff1count)
        for rand in rand_diff1:
            exam.questions.add(Question.objects.get(id=rand))

        diff2 = Question.objects.filter(difficulty=2).values_list('id', flat=True)
        rand_diff2 = random.sample(list(diff2), exam.diff2count)
        for rand in rand_diff2:
            exam.questions.add(Question.objects.get(id=rand))

        diff3 = Question.objects.filter(difficulty=3).values_list('id', flat=True)
        rand_diff3 = random.sample(list(diff3), exam.diff3count)
        for rand in rand_diff3:
            exam.questions.add(Question.objects.get(id=rand))

        diff4 = Question.objects.filter(difficulty=4).values_list('id', flat=True)
        rand_diff4 = random.sample(list(diff4), exam.diff4count)
        for rand in rand_diff4:
            exam.questions.add(Question.objects.get(id=rand))

        diff5 = Question.objects.filter(difficulty=5).values_list('id', flat=True)
        rand_diff5 = random.sample(list(diff5), exam.diff5count)
        for rand in rand_diff5:
            exam.questions.add(Question.objects.get(id=rand))

        exam.save()
        return HttpResponseRedirect(reverse('course:show_exam') + '?id=' + str(exam.id))


def delete_exam(request):
    exam = Exam.objects.get(id=request.GET['id'])
    exam.delete()
    return HttpResponseRedirect(reverse('course:exams'))


def show_exam(request):
    exam_id = request.GET['id']
    exam = Exam.objects.get(id=exam_id)
    return render(request, 'show_exam.html', {'exam': exam, 'questions': Question.objects.filter(exams=exam)})


def save_exam(request):
    exam_id = request.GET['id']
    exam = Exam.objects.get(id=exam_id)
    exam.saved = True
    exam.save()
    return HttpResponseRedirect(reverse('course:exams'))
