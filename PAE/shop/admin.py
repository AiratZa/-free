from django.contrib import admin
from .models import Shop, Sale, UserInfo, Tag, Category
# Register your models here.

admin.site.register([Shop, Sale, Tag, UserInfo, Category])