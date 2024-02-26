from django.contrib import admin
from apps.base.models import Settings, News, Blog
# Register your models here.

admin.site.register(Settings)
admin.site.register(News)
admin.site.register(Blog)