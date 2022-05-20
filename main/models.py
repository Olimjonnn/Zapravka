from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'Director'),
        (2, 'Manager'),
        (3, 'User'),
    ), default=3)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Info(models.Model):
    logo = models.ImageField(upload_to="Info")
    phone = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    telegram_link = models.CharField(max_length=500)
    instagram_link = models.CharField(max_length=500)

class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True, null=True)
    payed  = models.IntegerField()
    discon_card = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Benzin(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    quantity = models.IntegerField()

class BenzinProduction(models.Model):
    benzin = models.ForeignKey(Benzin, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    allow = models.IntegerField(choices=(
        (1, "Ready"),
        (2, "Accept"),
        (3, "Refuse"),
    ), default=1)
    day = models.DateField(auto_now_add=True)

class Cash(models.Model):
    cash = models.IntegerField(default=0)


class Pay(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    benzin = models.ForeignKey(Benzin, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    image = models.ImageField(upload_to="News/")
    text = models.TextField()
    


