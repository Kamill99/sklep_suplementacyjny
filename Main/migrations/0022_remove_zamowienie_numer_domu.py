# Generated by Django 3.2.9 on 2022-11-13 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0021_auto_20221113_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zamowienie',
            name='numer_domu',
        ),
    ]
