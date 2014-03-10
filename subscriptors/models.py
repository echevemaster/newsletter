from django.db import models

from provider.oauth2.models import Client


class Attributes(models.Model):
    name = models.CharField(max_length=255)
    app = models.ForeignKey(Client)

    def __unicode__(self):
        return self.name


class Subscriptor(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blacklist', 'Black List'),
    )
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(primary_key=True)
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    attributes = models.ManyToManyField(Attributes)
    apps = models.ManyToManyField(Client)

    def __unicode__(self):
        return self.username
