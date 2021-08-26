from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('w3band', views.w3band, name='page2'),
    path('w3result', views.w3result, name = 'w3result'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout' ,views.logout, name = 'logout')
]
