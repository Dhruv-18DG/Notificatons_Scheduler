from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name=""),
    path('register', register, name="register"),
    path('my-login', my_login, name="my-login"),
    path('dashboard', homepage, name="dashboard"),
]