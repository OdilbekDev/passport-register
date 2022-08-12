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


def Register(request):
    return render(request, 'register.html')


def Create_User(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    father_name = request.POST['father_name']
    username = request.POST['username']
    password = request.POST['password']
    phone = request.POST['phone']
    telegram_id = request.POST['telegram_id']
    address = request.POST['address']
    age = request.POST['age']
    gender = request.POST['gender']

    User.objects.create(
        first_name=first_name, last_name=last_name, father_name=father_name, username=username, password=password, phone=phone, telegram_id=telegram_id, address=address, age=age, gender=gender
    )

    return redirect('index')

def navbat(request):
    return render(request, 'customer-wishlist.html')

def detail(request):
    return render(request, 'detail.html')


def View_Queue(request):
    user = request.user
    queue = Queue.objects.get(user=user)
    context = {
        'queue': queue,
    }
    return render(request, 'faq.html', context)