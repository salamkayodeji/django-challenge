# Generated by Django 3.2.5 on 2021-08-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'name', 'verbose_name_plural': 'names'},
        ),
    ]
