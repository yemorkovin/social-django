from django.db import models


class User(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    login = models.CharField(max_length=200, verbose_name='Login')
    password = models.CharField(max_length=200, verbose_name='Password')
    avatar = models.ImageField(upload_to='soc/social/avatars', verbose_name='Аватарка')
    dateb = models.DateField(verbose_name='Дата рождения')
    city = models.CharField(max_length=200, verbose_name='Город')


class Panel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', default='')
    description = models.CharField(max_length=200, verbose_name='Описание', default='')
    image = models.ImageField(upload_to='soc/social/panels', verbose_name='Картинка')
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
