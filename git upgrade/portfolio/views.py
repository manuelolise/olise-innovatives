from django.shortcuts import render
from portfolio.models import Contact

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        #ins stands for instance, we are creating an instance for an our class contact and 
        #we are importing it from portfolio.models
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been created to db")
    return render(request, 'portfolio/contact.html')

def project(request):
    return render(request, 'portfolio/project.html')

def projectsingle1(request):
    return render(request, 'portfolio/projectsingle1.html')

def projectsingle2(request):
    return render(request, 'portfolio/projectsingle2.html')

def projectsingle3(request):
    return render(request, 'portfolio/projectsingle3.html')

def projectsingle4(request):
    return render(request, 'portfolio/projectsingle4.html')

def projectsingle5(request):
    return render(request, 'portfolio/projectsingle5.html')

def projectsingle6(request):
    return render(request, 'portfolio/projectsingle6.html')

def projectsingle7(request):
    return render(request, 'portfolio/projectsingle7.html')

def projectsingle8(request):
    return render(request, 'portfolio/projectsingle8.html')

def projectsingle9(request):
    return render(request, 'portfolio/projectsingle9.html')

def projectsingle10(request):
    return render(request, 'portfolio/projectsingle10.html')


