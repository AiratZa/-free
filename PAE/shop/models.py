from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name = 'Прошел активацию?')
    send_messages = models.BooleanField(default = True, verbose_name='Слать оповещения о новых акциях и скидках в любимых категориях?')

    class Meta (AbstractUser.Meta):
        pass


class Shop(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField 
    

class Sale (models.Model):
    size = models.DecimalField (max_digits = 5, decimal_places = 2)
    TYPES_OF_SALE = (
        ('p', 'Процент от цены'),
        ('a', 'Сумма скидки')
    )
    TYPES_OF_CURRENCY = (
        ('RR', 'Российский рубль'),
        ('USD', 'American dollar'),
        ('EUR', 'Euro'), 
    )
    type_of_sale = models.CharField(max_length = 1, choices=TYPES_OF_SALE, )
    type_of_currency = models.CharField(max_length = 3, choices = TYPES_OF_CURRENCY, null=True, blank=True)
    url_for_sale = models.URLField
    about = models.TextField (max_length = 512)
    slug = models.SlugField
    date_posted = models.DateField (auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank=True)
    category = models.ManyToManyField('Category')
    was_changed = models.BooleanField
    date_changed = models.DateField (auto_now = True)
    changed_by = models.ForeignKey (UserInfo, on_delete = models.SET(False))

class Tag (models.Model):
    tag_name = models.CharField(max_length = 50)


class Category(models.Model):
    name = models.CharField(max_length = 30)