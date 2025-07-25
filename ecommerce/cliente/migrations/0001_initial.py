# Generated by Django 5.2.1 on 2025-07-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='correo')),
                ('contrasenia', models.CharField(max_length=128, verbose_name='contrasenia')),
                ('es_vendedor', models.BooleanField(default=False, verbose_name='es_vendedor')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
