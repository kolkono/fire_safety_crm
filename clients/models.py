from django.db import models

class Client(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Электронная почта')
    address = models.TextField('Адрес')
    city = models.CharField('Город', max_length=100, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
