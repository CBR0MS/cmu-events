from django.contrib import admin
from .models import Topic, Organization, Event

admin.site.register(Topic)
admin.site.register(Organization)
admin.site.register(Event)
# Register your models here.
