# Generated by Django 4.2 on 2023-05-16 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_rename_data_entrada_reservaday_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaday',
            name='servicos_adicionais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais'),
        ),
    ]
