# Generated by Django 3.2.9 on 2022-11-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0022_remove_zamowienie_numer_domu'),
    ]

    operations = [
        migrations.CreateModel(
            name='KodyRabatowe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Kod rabatowy',
                'verbose_name_plural': 'Kody rabatowe',
            },
        ),
    ]
