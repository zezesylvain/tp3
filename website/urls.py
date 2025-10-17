from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('l3info', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
]