from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_login),
    path('registration', views.registration),
    path('login', views.login),
    path('mainboard', views.mainboard),
    path('logout', views.logout),
    path('event/<int:event_id>', views.event),
    path('add_event', views.add_event)
]