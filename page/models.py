from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=55, db_index=True, verbose_name="Имя")
    surname = models.CharField(max_length=55, db_index=True, verbose_name="Фамилия")
    email = models.EmailField(db_index=True, verbose_name="Почта")
    login = models.CharField(max_length=55, db_index=True, verbose_name="Логин")
    password = models.CharField(max_length=55, db_index=True, verbose_name="Пароль")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.login} - {self.password}"






