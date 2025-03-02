from django.shortcuts import render
from .models import Course
from django.urls import reverse_lazy
from django.views.generic import *

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = "course"

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "delete_course.html"
    context_object_name = "course"
    success_url = reverse_lazy("course_list")
