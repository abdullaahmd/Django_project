from django.shortcuts import render
#from django.http import HttpResponse
context = [
    {
        'author' : 'mohamed',
        'title' : 'Blog Post 1',
        'content' : 'First Blog content',
        'date_posted' : 'February 7 2020'
    },
    {
        'author' : 'abdullah',
        'title' : 'Blog Post 2',
        'content' : 'Second Blog content',
        'date_posted' : 'February 6 2020'
    }
]
def home(request):
    return render(request, 'blog/home.html', {'posts':context})
    #return HttpResponse('<h1> Welcome to blog home!</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    return HttpResponse('<h1> Welcome to blog about!</h1>')
# Create your views here.
