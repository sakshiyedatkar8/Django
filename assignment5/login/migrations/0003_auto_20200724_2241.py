# Generated by Django 3.0.8 on 2020-07-24 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200724_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='address',
            new_name='mail',
        ),
    ]