from django.contrib import admin

from .models import WebHookHistory, AppHistory


class WebHookHistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'action', 'subscriptor')
    list_filter = ('name', 'action', 'date')
    search_fields = ('subscriptor',)


class AppHistoryAdmin(admin.ModelAdmin):
    list_display = ('action', 'app')
    list_filter = ('action', 'app')
    search_fields = ('action',)


admin.site.register(WebHookHistory, WebHookHistoryAdmin)
admin.site.register(AppHistory, AppHistoryAdmin)
