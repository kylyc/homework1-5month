from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    blog = News.objects.all()
    return render(request, "demo25.html", locals())

def blog(request):
    blog = News.objects.all()
    blog = Blog.objects.latest('id')
    return render(request, "blog-post.html", locals())

def signin(request):
    return render(request, "signin.html", locals()) 

def signup(request):
    return render(request, "signup.html", locals())

