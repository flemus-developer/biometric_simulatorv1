# Generated by Django 3.0 on 2021-08-18 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_auto_20210817_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'db_table': 'register',
            },
        ),
    ]