from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register_login(request):
    return render(request, 'index.html')
