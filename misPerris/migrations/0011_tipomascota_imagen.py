# Generated by Django 3.2 on 2021-05-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0010_alter_mascota_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='tipos'),
        ),
    ]
