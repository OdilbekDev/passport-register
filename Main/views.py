from django.shortcuts import redirect, render
from Main.models import *

# Create your views here.
def Index(request):
    slider = Slider.objects.last()
    service = Service.objects.filter().order_by('-id')[:3]
    blog = Blog.objects.all()
    lastblog = Blog.objects.last()
    gallery = Gallery.objects.all()
    context = {
        'slider': slider,
        'service': service,
        'blog': blog,
        'lastblog': lastblog,
        'gallery': gallery,
    }

    return render(request, 'index.html', context)


def About(request):
    return render(request, 'about.html')


def Send_Application(request):
    
    return render(request, 'application.html')



def Create_Application(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    passport_father = request.POST['passport_father']
    passport_mother = request.POST['passport_mother']
    cadastre = request.POST['cadastre']
    user = request.user
    Application_Citizenship.objects.create(first_name=first_name, last_name=last_name, passport_father=passport_father, passport_mother=passport_mother, cadastre=cadastre, user=user)
    print(True)

    return redirect('index')



def Send_Application_migration(request):
    
    return render(request, 'application_migration.html')




def Create_Application_Migration(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    id_card = request.POST['id_card']
    address = request.POST['address']
    agreement_father = request.POST['agreement_father']
    agreement_mother = request.POST['agreement_mother']
    address = request.POST['address']
    user = request.user
    Application_Migration.objects.create(first_name=first_name, last_name=last_name, id_card=id_card, address=address, agreement_father=agreement_father, agreement_mother=agreement_mother, user=user)
    print(True)

    return redirect('index')


def Create_Application_Migration_Older(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    id_card = request.POST['id_card']
    user = request.user
    Application_Migration_Older.objects.create(first_name=first_name, last_name=last_name, id_card=id_card, user=user)
    print(True)

    return redirect('index')