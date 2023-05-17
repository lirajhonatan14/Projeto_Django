# Generated by Django 4.2 on 2023-05-16 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0001_initial'),
        ('hotel', '0002_remove_servicosadicionais_num_reserva_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservaday',
            old_name='data_entrada',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='reservaday',
            name='data_saida',
        ),
        migrations.AddField(
            model_name='reservaday',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ficha.fichadog'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='reservaday',
            name='servicos_adicionais',
        ),
        migrations.CreateModel(
            name='ReservaServicoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.reserva')),
                ('servico_adicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais')),
            ],
            options={
                'db_table': 'Reserva_Servicos_adicionais',
            },
        ),
        migrations.AddField(
            model_name='reservaday',
            name='servicos_adicionais',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais'),
            preserve_default=False,
        ),
    ]