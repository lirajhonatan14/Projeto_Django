# Generated by Django 4.2 on 2023-05-01 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservaday',
            old_name='dog_id',
            new_name='dog',
        ),
    ]
