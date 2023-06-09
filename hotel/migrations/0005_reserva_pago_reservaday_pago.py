# Generated by Django 4.2 on 2023-05-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_reservaday_servicos_adicionais'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='pago',
            field=models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='reservaday',
            name='pago',
            field=models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False, null=True),
        ),
    ]
