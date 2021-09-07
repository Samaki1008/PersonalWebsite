from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'sammed',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'june 14 2021'

    },
    {
        'author': 'sneha',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'july 14 2021'

    }

]

def home(request):

    context = {

        'post': Post.objects.all()

    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'post': Post.objects.all()

    }
    return render(request, 'about.html', context)
