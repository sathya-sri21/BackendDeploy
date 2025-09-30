from django.shortcuts import render

def welcome_page(request):
    return render(request,'index.html')
def about_page(request):
    return render(request,'about.html')