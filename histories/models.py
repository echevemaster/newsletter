from django.db import models

from provider.oauth2.models import Client

from subscriptors.models import Subscriptor


class WebHookHistory(models.Model):
    """ Model to keep track of the calls by webhooks
        like Mandrill or SendGrid
    """
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    subscriptor = models.ForeignKey(Subscriptor)

    def __unicode__(self):
        return self.name


class AppHistory(models.Model):
    """ Model to keep track of the calls by apps
        like Platzi or Mejorando.la
    """
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(Client)

    def __unicode__(self):
        return self.action
