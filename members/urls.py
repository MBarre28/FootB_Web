from django.urls import path
from .views import members, details, main, nav, testing

urlpatterns = [
    path('members/', members, name='members'),
    path('members/details/<int:id>', details, name='details'),
    path('', main, name='main'),
    path('nav/', nav, name='nav'),
    path('testing/', testing, name='testing'),

]
