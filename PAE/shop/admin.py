from django.contrib import admin
from .models import Shop, Sale, Tag, Category

import datetime

from .models import UserInfo
from .utilities import send_activation_notification

# Register your models here.

admin.site.register([Tag, Category])

def send_activation_notifications(modeladmin, request, queryset):
    for rec in quetyset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письма с оповещениями отправлены')

send_activation_notifications.short_description = 'Отправка писем с оповещением об активации'

class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Прошли активацию?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3 дней'),
            ('week', 'Не прошли более недели')
        )
    
    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active = True, is_activated = True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days = 3)
            return queryset.filter(is_active = False, is_activated = False, date_joined__date__lt = d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks = 1)
            return queryset.filter(is_active = False, is_activated = False, date_joined__date__lt = d)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
               ('send_messages', 'is_active', 'is_activated'),
               ('is_staff', 'is_superuser'),
               'groups', 'user_permissions',
               ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)

admin.site.register(UserInfo, UserInfoAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('shop', 'title', 'from_exct_until', 'size', 'sale_measure')
    fields = (('shop','title'), ('from_exct_until', 'size', 'sale_measure'),('promocode', 'valid_until'),
               ('about'),('url_for_sale', 'slug'),
               ('tag', 'category'), 'changed_by', 'date_created')
    readonly_fields = ('date_created',)


admin.site.register(Sale, SaleAdmin)


admin.site.register(Shop)
