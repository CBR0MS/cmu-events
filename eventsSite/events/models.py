from django.db import models
#from eventsSite.accounts.models import User


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=30, blank=True)
    topics = models.ManyToManyField(Topic)
    members = models.ManyToManyField('accounts.User')

    def __str__(self):
        return self.name


class Event(models.Model):
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    img_url = models.URLField()

    def __str__(self):
        return self.name


