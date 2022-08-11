from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    extra_phone = models.CharField(max_length=255, null=True, blank=True)
    telegram_id = models.IntegerField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Application_Citizenship(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_document = models.FileField(upload_to="documents/birth_documents/")
    passport_father = models.FileField(upload_to="documents/parents_passport/")
    passport_mother = models.FileField(upload_to="documents/parents_passport/")
    cadastre = models.FileField(upload_to="documents/cadastres/")
    status = models.IntegerField(
        choices=(
            (0, 'Sent'),
            (1, 'Confirmed'),
            (2, 'Registred'),
            (3, 'Printed')
        ), default=0
    )

    def __str__(self):
        return self.user.username


class Application_Migration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_card = models.FileField(upload_to="documents/ID_cards/")
    agreement_father = models.FileField(upload_to="documents/parents_passport/")
    agreement_mother = models.FileField(upload_to="documents/parents_passport/")
    status = models.IntegerField(
        choices=(
            (0, 'Sent'),
            (1, 'Confirmed'),
            (2, 'Registred'),
            (3, 'Printed')
        ), default=0
    )

    def __str__(self):
        return self.first_name


class Application_Migration_Older(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_card = models.FileField(upload_to="documents/ID_cards/")
    status = models.IntegerField(
        choices=(
            (0, 'Sent'),
            (1, 'Confirmed'),
            (2, 'Registred'),
            (3, 'Printed')
        ), default=0
    )

    def __str__(self):
        return self.first_name


class Queue_Citizenship(models.Model):
    application = models.ForeignKey(Application_Citizenship, on_delete=models.CASCADE)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Queue_Migration(models.Model):
    application = models.ForeignKey(Application_Migration, on_delete=models.CASCADE)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Slider(models.Model):
    img1 = models.ImageField(upload_to="slider/")
    img2 = models.ImageField(upload_to="slider/")
    img3 = models.ImageField(upload_to="slider/")




class Service(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Gallery(models.Model):
    img = models.ImageField(upload_to="galleries/")


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    img = models.ImageField(upload_to="img/blog/")
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    img2 = models.ImageField(upload_to="img/blog/")
    text2 = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message


class Reply_Comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Info(models.Model):
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
