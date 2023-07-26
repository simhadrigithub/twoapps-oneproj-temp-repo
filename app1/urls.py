
from django.urls import path
from app1.views import *

urlpatterns =[
    path('hello/',hello,name='hello'),
    path('beauty/',beauty,name='beauty'),
]