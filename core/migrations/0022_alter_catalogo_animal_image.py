# Generated by Django 4.1.6 on 2023-02-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_catalogo_animal_image_alter_animal_animal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='animal_image',
            field=models.ImageField(blank=True, null=True, upload_to='animal_catalogo/', verbose_name='Foto do animal (opcional)'),
        ),
    ]
