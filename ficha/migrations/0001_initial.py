# Generated by Django 4.2 on 2023-05-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FichaDog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=1)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo_alimentacao', models.CharField(max_length=100)),
                ('restricoes_alimentares', models.CharField(blank=True, max_length=100, null=True)),
                ('contato_proprietario', models.CharField(max_length=100)),
                ('endereco', models.TextField(max_length=100)),
                ('veterinario_cao', models.CharField(blank=True, max_length=100, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(max_length=100)),
            ],
            options={
                'db_table': 'Ficha_Dog',
            },
        ),
    ]
