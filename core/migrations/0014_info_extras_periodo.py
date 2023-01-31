# Generated by Django 3.2.13 on 2023-01-30 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_errante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervalo', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alimentacao_tipo', models.CharField(blank=True, max_length=128, null=True, verbose_name='Tipo de alimentação')),
                ('condicoes', models.CharField(max_length=128, verbose_name='Condições de abrigo na residência')),
                ('dt_vacinacao', models.DateField(blank=True, null=True, verbose_name='Data da última vacinação')),
                ('dt_vermifugacao', models.DateField(blank=True, null=True, verbose_name='Data da última vermifugação')),
                ('complemento', models.CharField(blank=True, max_length=256, null=True, verbose_name='Complemento')),
                ('dt_registro', models.DateField(blank=True, null=True, verbose_name='Data do registro')),
                ('alimentacao_periodo', models.ManyToManyField(to='core.Periodo', verbose_name='Período da alimentação')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.animal')),
            ],
            options={
                'ordering': ['animal'],
            },
        ),
    ]