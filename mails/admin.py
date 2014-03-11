from django.contrib import admin

from .models import MailTemplate, Mail


class MailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)
    search_fields = ('name',)


class MailAdmin(admin.ModelAdmin):
    list_display = ('to', 'subject', 'approved', 'sent', 'app')    
    list_filter = ('app', 'approved', 'sent')
    search_fields = ('to',)


admin.site.register(MailTemplate, MailTemplateAdmin)
admin.site.register(Mail, MailAdmin)
