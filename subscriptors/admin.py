from django.contrib import admin

from .models import Attributes, Subscriptor


class AttributesAdmin(admin.ModelAdmin):
    list_display = ('name', 'app')
    list_filter = ('app',)
    search_fields = ('name',)


class SubscriptorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'status',)
    list_filter = ('status', 'apps',)
    search_fields = ('username', 'email',)


admin.site.register(Attributes, AttributesAdmin)
admin.site.register(Subscriptor,  SubscriptorAdmin)
