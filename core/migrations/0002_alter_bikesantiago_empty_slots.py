# Generated by Django 4.1.7 on 2023-02-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikesantiago',
            name='empty_slots',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]