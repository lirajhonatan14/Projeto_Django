# Generated by Django 4.2 on 2023-05-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservaday',
            name='id',
        ),
        migrations.AlterField(
            model_name='reservaday',
            name='num_reserva',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]