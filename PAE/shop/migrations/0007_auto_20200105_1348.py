# Generated by Django 3.0.2 on 2020-01-05 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200105_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='date_posted',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='date_changed',
        ),
    ]
