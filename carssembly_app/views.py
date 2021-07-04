from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def register_login(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        errors = User.objects.login_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
                return redirect('/')
        if not User.objects.authenticate(email, password):
            messages.error(request, 'your email and password did not match our records')
            return redirect('/')
    user = User.objects.get(email=email)
    print(user.email)
    request.session['user_firstname'] = user.firstname
    request.session['user_id'] = user.id
    return redirect('/mainboard')

def mainboard(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1>Log in using your account dummy</h1>')
    return render(request, 'mainboard.html')

def logout(request):
    del request.session['user_id']
    request.session.clear()
    return redirect('/')

def registration(request):
    errors = User.objects.register_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect('/')
    if not len(errors):
        messages.success(request, 'You have registered successfully')
        return redirect('/')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nickname = request.POST['nickname']
        age = request.POST['age']
        hometown = request.POST['hometown']
        email = request.POST['email']
        password = request.POST['password']
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(firstname=firstname, lastname=lastname, nickname=nickname, age=age, hometown=hometown, email=email, password=hash_pw)
        return redirect('/')

def event(request):
    return render(request, 'event.html')