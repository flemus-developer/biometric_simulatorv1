# Generated by Django 3.0 on 2021-08-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Juan, María, Pedro', max_length=10, verbose_name='Nombre')),
                ('surname', models.CharField(help_text='Morales, España, Gómez', max_length=10, verbose_name='Apellido')),
            ],
        ),
    ]