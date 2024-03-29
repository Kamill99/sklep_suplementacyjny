# Generated by Django 3.2.9 on 2022-11-13 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_zamowienie'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamowienie',
            name='imie',
            field=models.CharField(default="a", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='kod_pocztowy',
            field=models.CharField(default="a", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='miasto',
            field=models.CharField(default="a", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='nazwisko',
            field=models.CharField(default="a", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='numer_domu',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zamowienie',
            name='numer_telefonu',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
