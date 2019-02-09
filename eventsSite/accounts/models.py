from django.db import models
from django.contrib.auth.models import AbstractUser
# from eventsSite.events.models import Organization
import requests

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    organizations = models.ManyToManyField('events.Organization')
    # topics_of_interest = models.ManyToManyField()
    # organizations = models.ManyToManyField()

    def save(self, *args, **kwargs):

        query = 'https://apis.scottylabs.org/directory/v1/andrewID/' + self.username + '/raw'
        response = requests.get(query)
        if response.status_code == 200:
            data = response.json()
            try:
                self.first_name = data['givenName']
                self.last_name = data['sn']
                #self.department = data['cmuDepartment']
            except KeyError as e:
                #do nothing 
                pass

        super().save(*args, **kwargs)