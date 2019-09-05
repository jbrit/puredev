from django.shortcuts import render

def home(request):
    return render(request,"puredev/page.html")

def project(request):
    return render(request, "puredev/project.html")