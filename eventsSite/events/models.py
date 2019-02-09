from django.db import models
#from eventsSite.accounts.models import User


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=30, blank=True)
    #topics = models.ManyToManyField(Topic)
    members = models.ManyToManyField('accounts.User',null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    slug = models.SlugField(unique=True, null=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30,null=True)
    date = models.DateField(auto_now=False, null=True)
    time = models.TimeField(auto_now=False, null=True)
    dateE = models.CharField(max_length=30, null=True)
    timeE = models.CharField(max_length=30, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    img_url = models.URLField()

    def __str__(self):
        return self.name
