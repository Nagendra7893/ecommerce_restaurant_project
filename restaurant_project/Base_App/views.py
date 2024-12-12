from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'home.html')

def AboutViews(request):
    pass

def MenuViews(request):
    pass

def BookTableViews(request):
    pass