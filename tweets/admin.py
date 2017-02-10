from django.contrib import admin
from models import Tweet
admin.site.register(Tweet)


def __unicode__(self):
    return self.text
