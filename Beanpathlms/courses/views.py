from django.shortcuts import render
from django.views import generic

from .models import Course

# Create your views here.

class IndexView(generic.ListView):  
    template_name = "courses/index.html"
    context_object_name = "course_list"

    def  get_queryset(self):
        return Course.objects.all()[:5]

class CourseView(generic.DetailView):
    model = Course
    template_name = "courses/course.html"