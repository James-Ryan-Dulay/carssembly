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
    request.session['user_firstname'] = user.firstname
    request.session['user_id'] = user.id
    return redirect('/mainboard')

def mainboard(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1>Log in using your account dummy</h1> <a href="/"> Login </a>')
    context = {
        'events' : Event.objects.all()
    }
    return render(request, 'mainboard.html', context)

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
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        nickname = request.POST['nickname']
        age = request.POST['age']
        hometown = request.POST['hometown']
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(hash_pw)
        User.objects.create(firstname=firstname, lastname=lastname, nickname=nickname, age=age, hometown=hometown, email=email, password=hash_pw)
        if not len(errors):
            messages.success(request, 'You have registered successfully')
        return redirect('/')

def event(request, event_id):
    if 'user_id' not in request.session:
        return HttpResponse('<h1> please login using your account </h1> <a href="/"> Login </a>')
    context = {
        'event' : Event.objects.get(id=event_id)
    }
    return render(request, 'event.html', context)

def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        description = request.POST['description']
        user = User.objects.get(id=request.session['user_id'])
        Event.objects.create(title=title, date=date, time=time, location=location, description=description, user=user)
        return redirect('/mainboard')

def user_join(request, event_id):
    event = Event.objects.get(id=event_id)
    user = request.session['user_id']
    event.join.add(user)
    return redirect('/mainboard')

def user_interest(request, event_id):
    event = Event.objects.get(id=event_id)
    user = request.session['user_id']
    event.interest.add(user)
    return redirect('/mainboard')

def add_discussion(request, event_id):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        event = Event.objects.get(id=event_id)
        discuss = request.POST['discuss']
        Discuss.objects.create(discuss=discuss, user=user, event=event)
        return redirect(f'/event/{event_id}')

def discuss_delete(request, discuss_id, event_id):
    discuss = Discuss.objects.get(id=discuss_id)
    discuss.delete()
    return redirect(f'/event/{event_id}')