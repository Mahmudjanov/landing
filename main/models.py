from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    photo = models.ImageField()

    def str(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    icon_code = models.CharField(max_length=66, help_text='icon-icons')

class About(models.Model):
    l_text = models.TextField()
    r_text = models.TextField()
    photo = models.ImageField()


class Portfolio(models.Model):
    photo = models.ImageField()

class Testimonials(models.Model):
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Client(models.Model):
    photo = models.ImageField()


class Conatact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    massage = models.CharField(max_length=255)

class Smedia(models.Model):
    smedia = models.CharField(max_length=255)

class Address(models.Model):
    address = models.CharField(max_length=255)

class Form(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Information(models.Model):
    adres = models.CharField(max_length=255)
    tw = models.URLField()
    fb = models.URLField()
    insta = models.URLField()
    dribble = models.URLField()
    ln = models.URLField()