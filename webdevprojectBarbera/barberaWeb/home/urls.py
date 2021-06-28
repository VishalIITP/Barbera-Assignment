from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('bookings', views.bookings, name='bookings'),
    path('myCart', views.myCart, name='myCart'),

    path('register', views.registerPage, name='registration'),
    path('login', views.loginPage, name='login'),

    path('polls', views.polls, name='polls'),

]
