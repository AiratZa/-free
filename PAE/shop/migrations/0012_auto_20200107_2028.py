# Generated by Django 3.0.2 on 2020-01-07 17:28

from django.db import migrations, models
import shop.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200107_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='logo_img',
            field=models.ImageField(blank=True, upload_to=shop.utilities.get_timestamp_path, verbose_name='Логотип магазина'),
        ),
    ]
