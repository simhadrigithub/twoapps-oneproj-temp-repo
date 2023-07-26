from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,"hello.html")

def beauty(request):
    return render(request,"beauty.html")
