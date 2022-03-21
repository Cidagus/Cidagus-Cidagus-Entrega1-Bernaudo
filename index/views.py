from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    return render(request,"index/index.html")

def blogpage(request):
    return render(request,"index/about.html")    