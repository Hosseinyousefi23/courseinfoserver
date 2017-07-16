from django.conf.urls import url

from course import views


app_name = "course"

urlpatterns = \
    [
        url(r'^$', views.main_page, name='main_page'),
        url(r'^students$', views.students, name='students'),
        url(r'^profs$', views.profs, name='profs'),
        url(r'^courses$', views.courses, name='courses'),
        url(r'^edit_student$', views.edit_student, name='edit_student'),
        url(r'^edit_prof$', views.edit_prof, name='edit_prof'),
        url(r'^edit_course$', views.edit_course, name='edit_course'),
        url(r'^add_student$', views.add_student, name='add_student'),
        url(r'^add_prof$', views.add_prof, name='add_prof'),
        url(r'^add_course$', views.add_course, name='add_course'),
        url(r'^delete_student$', views.delete_student, name='delete_student'),
        url(r'^delete_prof$', views.delete_prof, name='delete_prof'),
        url(r'^delete_course$', views.delete_course, name='delete_course'),
        url(r'^search$', views.search, name='search'),

    ]

