from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    data = models.ForeignKey(User, on_delete=models.CASCADE, related_name='da', blank=True, null=True)
    name = models.CharField(max_length=55, db_index=True, verbose_name="Имя")
    surname = models.CharField(max_length=55, db_index=True, verbose_name="Фамилия")
    email = models.EmailField(db_index=True, verbose_name="Почта")
    login = models.CharField(max_length=55, db_index=True, verbose_name="Логин")
    password = models.CharField(max_length=55, db_index=True, verbose_name="Пароль")

    class Meta:
        ordering = ('login',)

    def __str__(self):
        return f"{self.login} - {self.password}"






