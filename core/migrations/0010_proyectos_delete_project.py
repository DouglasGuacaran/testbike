# Generated by Django 4.1.7 on 2023-02-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.CharField(max_length=250)),
                ('Nombre', models.CharField(max_length=255)),
                ('Tipo', models.CharField(max_length=250)),
                ('Region', models.CharField(max_length=250)),
                ('Tipologia', models.CharField(max_length=255)),
                ('Titular', models.CharField(max_length=255)),
                ('Inversion', models.CharField(max_length=255)),
                ('FechaPresentacionFecha', models.CharField(max_length=255)),
                ('Estado', models.CharField(max_length=230)),
                ('Mapa', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
