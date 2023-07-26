from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def trees(request):
    return render(request,'trees.html')