from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from . models import Course, Subjects
from django.db import models
# Create your views here.
def index(request):
    
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def courses(request):
    all_courses = Course.objects.all()
    # all_subjects = Subjects.objects.all()
    all_subjects = Subjects.objects.annotate(course_count=models.Count('course'))
    
    context = {"allcourses":all_courses,"allsubjects":all_subjects}
    
    
    return render(request,'course.html',context)


def teachers(request):
    return render(request,'teacher.html')


def contacts(request):
    return render(request,'contact.html')

def get_subjects(request):
    all_subjects = Subjects.objects.all().values()
    all_subjects_list =list(all_subjects)
    return JsonResponse({'subjects':all_subjects_list})
    