from django.db import models
import bcrypt, re

from django.db.models.deletion import CASCADE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validate(self, post_data):
        errors = {}
        if not len(post_data['firstname']) and not len(post_data['lastname']) and not len(post_data['nickname']) and not len(post_data['hometown']) and not len(post_data['email']) and not len(post_data['password']) and not len(post_data['confirm_password']):
            errors['all'] = 'please fill out all form'
            return errors
        if len(post_data['firstname']) <= 2:
            errors['firstname'] = 'enter a valid name or firstname should be more than 2 characters'
        if len(post_data['lastname']) <= 2:
            errors['lastname'] = 'enter a valid lastname or lastname should be more than 2 characters'
        if len(post_data['nickname']) <= 1:
            errors['nickname'] = 'nickname must contain at least 2 characters'
        if int(post_data['age']) < 18:
            errors['age'] = 'you must be at least 18 years old'
        if len(post_data['hometown']) < 3:
            errors['hometown'] = 'hometown must be more than 3 characters'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'email address not valid'
        if len(post_data['password']) < 8:
            errors['password'] = 'password needs to be more than 8 characters'
        if post_data['confirm_password'] != post_data['password']:
            errors['confirm_password'] = 'your password did not match'
        return errors

    def login_validate(self, post_data):
        errors = {}
        if not len(post_data['email']) and not len(post_data['password']):
            errors['all'] = 'please fill out the login form'
        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    hometown = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='events', on_delete = models.CASCADE)
    join = models.ManyToManyField(User, related_name='joins')
    interest = models.ManyToManyField(User, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.date} {self.time} {self.join}'

class Discuss(models.Model):
    discuss = models.TextField()
    user = models.ForeignKey(User, related_name='user_discuss', on_delete= models.CASCADE)
    event = models.ForeignKey(Event, related_name='event_discuss', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.discuss} {self.event}'