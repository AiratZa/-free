# Generated by Django 3.0.2 on 2020-01-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_shop_logo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='logo_img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Логотип магазина'),
        ),
    ]