# Generated by Django 5.2.1 on 2025-07-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_rename_precio_producto_precio_base_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=0, max_length=15, verbose_name='telefono'),
            preserve_default=False,
        ),
    ]
