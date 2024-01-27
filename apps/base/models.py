from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    image = models.ImageField(
        upload_to="portrait/",
        verbose_name="Фотография"
    )
    number1 = models.IntegerField(
        verbose_name='Цифры для Winning award (Награда)'
    )
    number2 = models.IntegerField(
        verbose_name='Цифры для Complete project (Полный проект)'
    )
    number3 = models.IntegerField(
        verbose_name='Цифры для Client review (Обзор клиента)'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок_2'
    )
    description1 = models.TextField(
        verbose_name='1_Описания заголовка_2 '
    )
    description2 = models.TextField(
        verbose_name='2_Описания заголовка_2 '
    )
    description3 = models.TextField(
        verbose_name='3_Описания заголовка_2 '
    )
    image2 = models.ImageField(
        upload_to='portrait1/',
        verbose_name='Фотография 2го заголовка'
    )
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name="Настройки сайта"
        verbose_name_plural="Настройки сайта"