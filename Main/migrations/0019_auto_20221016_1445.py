# Generated by Django 3.2.9 on 2022-10-16 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0018_elementzamowienia_zamwowienie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementKoszyka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Element koszyka',
                'verbose_name_plural': 'Elementy koszyka',
            },
        ),
        migrations.CreateModel(
            name='Koszyk',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('zamowione', models.BooleanField(default=False)),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Koszyk',
                'verbose_name_plural': 'Koszyk',
            },
        ),
        migrations.RemoveField(
            model_name='zamwowienie',
            name='elementy',
        ),
        migrations.RemoveField(
            model_name='zamwowienie',
            name='klient',
        ),
        migrations.DeleteModel(
            name='ElementZamowienia',
        ),
        migrations.DeleteModel(
            name='Zamwowienie',
        ),
        migrations.AddField(
            model_name='elementkoszyka',
            name='koszyk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='Main.koszyk'),
        ),
        migrations.AddField(
            model_name='elementkoszyka',
            name='produkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Main.supplement'),
        ),
    ]
