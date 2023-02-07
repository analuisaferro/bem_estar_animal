# Generated by Django 4.1.6 on 2023-02-07 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0007_pessoa_remove_tutor_user'),
        ('core', '0027_entrevistaprevia_animal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_moradia', models.CharField(choices=[('Própria', 'Própria'), ('Alugada', 'Alugada')], max_length=7, verbose_name='Tipo de moradia')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tutor'),
        ),
    ]