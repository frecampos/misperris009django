# Generated by Django 3.2 on 2021-04-30 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('nombre', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('annos', models.IntegerField()),
            ],
        ),
    ]