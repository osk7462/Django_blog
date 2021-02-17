from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.

def index(request):
    context = {
        'title':'Django_blog',
        'posts': Blog.objects.all(),
    }
    return render(request, 'home/index.html',context)


def about(request):
    return render(request, 'home/about.html', {})


def new_post(request):
    return render(request, 'home/new_post.html', {})


def profile(request):
    return render(request, 'home/profile.html', {})


def logoout(request):
    return HttpResponse("logout")

    

    

    