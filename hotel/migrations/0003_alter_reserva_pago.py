# Generated by Django 4.2.1 on 2023-05-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_reserva_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='pago',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
