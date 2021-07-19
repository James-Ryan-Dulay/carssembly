from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'nickname', 'age', 'hometown', 'email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'description', 'user', 'created_at')

@admin.register(Discuss)
class DiscussAdmin(admin.ModelAdmin):
    list_display = ('discuss', 'user', 'event', 'created_at', 'update_at')
