# Generated by Django 4.2.5 on 2023-09-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
