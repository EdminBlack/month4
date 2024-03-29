# Generated by Django 5.0.1 on 2024-01-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_settings_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.TextField(verbose_name='3_Описания заголовка_2 '),
        ),
        migrations.AlterField(
            model_name='settings',
            name='image',
            field=models.ImageField(upload_to='portrait1/', verbose_name='Фотография 2го заголовка'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Заголовок_2'),
        ),
    ]
