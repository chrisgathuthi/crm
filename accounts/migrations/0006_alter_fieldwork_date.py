# Generated by Django 4.2.6 on 2023-11-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_fieldwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldwork',
            name='date',
            field=models.DateField(),
        ),
    ]