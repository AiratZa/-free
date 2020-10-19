from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.dispatch import Signal
from .utilities import send_activation_notification, get_timestamp_path

import datetime


class UserInfo(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name = 'Прошел активацию?')
    send_messages = models.BooleanField(default = True, verbose_name='Слать оповещения о новых акциях и скидках в любимых категориях?')

    class Meta (AbstractUser.Meta):
        verbose_name_plural = "Пользователи"
        verbose_name= "Пользователь"


class Shop(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField 
    logo_img = models.ImageField(blank=True, verbose_name = 'Логотип магазина', upload_to = get_timestamp_path)

    def __str__(self):
        return self.name
    class Meta:    
        verbose_name_plural = "Магазины"
        verbose_name= "Магазин"
        ordering = ('name',)



class Sale (models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, blank=True, null=True)
    SALE_MEASURE = (
        ('%%', 'Процент' ),
        ('RR', 'Российский рубль'),
        ('USD', 'American dollar'),
        ('EUR', 'Euro'), 
    )

    SIZE_FROM_EXCT_UNTIL = (
        ('>=', 'От'),
        ('==', 'Ровно'),
        ('<=', 'До'), 
    )

    from_exct_until = models.CharField(max_length = 2, choices=SIZE_FROM_EXCT_UNTIL, null=True, blank=True)
    size = models.DecimalField (max_digits = 5, decimal_places = 2)
    sale_measure = models.CharField(max_length = 3, choices = SALE_MEASURE, null=True, blank=True)
    promocode = models.CharField(max_length = 36, null=True, blank=True)
    url_for_sale = models.URLField(blank=True, null=True)
    title = models.CharField(max_length = 64, null=True, blank=True)
    about = models.TextField (max_length = 512)
    slug = models.SlugField(blank=True, null=True)
    date_created = models.DateField (auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank=True)
    category = models.ManyToManyField('Category')
    valid_until = models.DateTimeField(auto_now = False, verbose_name='Действителен до', default = datetime.date(2020,1,1))
    changed_by = models.ForeignKey (UserInfo, on_delete = models.SET(False))

    def __str__(self):
        return '%s - %.2f %s' % (self.shop, self.size, self.sale_measure)

    class Meta:    
        verbose_name_plural = "Купоны/скидки/акции"
        verbose_name= "Купон/скидка/акция"


class Tag (models.Model):
    tag_name = models.CharField(max_length = 50)
    class Meta:    
        verbose_name_plural = "Тэги"
        verbose_name= "Тэг"

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    class Meta:    
        verbose_name_plural = "Категории"
        verbose_name= "Категория"


user_registrated = Signal(providing_args=['instance'])

def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registrated.connect(user_registrated_dispatcher)