# Generated by Django 3.2.9 on 2022-02-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_auto_20220222_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='Main/static/images'),
        ),
    ]
