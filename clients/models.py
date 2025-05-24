from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$', message="Введите корректный номер телефона")]
    )
    email = models.EmailField(validators=[EmailValidator(message="Введите корректный email")])
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
