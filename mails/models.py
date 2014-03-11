from django.db import models

from provider.oauth2.models import Client


class MailTemplate(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Mail(models.Model):
    subject = models.CharField(max_length=255)
    to = models.TextField()
    from_email = models.CharField(max_length=255)
    data = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField()
    sent = models.BooleanField()
    template = models.ForeignKey(MailTemplate)
    app = models.ForeignKey(Client)

    def __unicode__(self):
        return self.subject
