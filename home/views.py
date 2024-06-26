from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def courses(request):
    return render(request,'course.html')


def teachers(request):
    return HttpResponse("This is the teachers page!")


def contacts(request):
    return render(request,'contact.html')