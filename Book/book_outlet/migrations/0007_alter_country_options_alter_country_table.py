# Generated by Django 5.0.6 on 2024-07-03 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_country_booklist_published_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True, 'verbose_name': 'ModelName', 'verbose_name_plural': 'ModelNames'},
        ),
        migrations.AlterModelTable(
            name='country',
            table='Country of the Authors',
        ),
    ]
