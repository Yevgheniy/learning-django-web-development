from django.contrib import admin
from models import Tweet, HashTag
# Register your models here,
admin.site.register(Tweet)
admin.site.register(HashTag)


def __unicode__(self):
    return self.text
