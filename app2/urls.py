from django.urls import path
from app2.views import *

urlpatterns =[
    path('home/',home,name='home'),
    path('trees/',trees,name='trees'),

]