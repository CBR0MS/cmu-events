from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .converter import *
#from converter import *
#from django.db import models
from .models import *
#from models import *
import requests
import datetime
from datetime import time

@shared_task
def gather_data():
    emails = retrieve()
    for i in range(len(emails)):
        e = emails[i]
        if i == 0:
            #print(e.activity[0])
            url = 'https://api.unsplash.com/search/photos?page=1&query='+e.activity[0]
            url = url.replace(" ","")
            #print(url)
            v = requests.get(url,auth=('bc801fb1ae69dd4c086f0a8591f9a876ddb4984bd72733eea80a76ade94e25a6','de3bd98be482c6efbf0e942a69be24894b591613e67b8430076b45dd6ebc85d2'))
            if(v.status_code == 200):
                vStar = v.json
                print(vStar)
                e.urlimage[0] = vStar.urls.small
                url = vStar.urls.small
        else:
            url = emails[0].urlimage[0]
        if (len(e.activity[0])>30):
            name = e.activity[0][len(e.activity[0])-30:len(e.activity[0])]
        else:
            name = e.activity[0]
        if (len(e.loc[0])>30):
            location = e.loc[0][len(e.loc[0])-30:len(e.loc[0])]
        else:
            location = e.loc[0]
        if (len(e.date[0])>30):
            dateE = e.date[0][len(e.date[0])-30:len(e.date[0])]
        else:
            dateE = e.date[0]
        if (len(e.time[0])>30):
            timeE = e.time[0][len(e.time[0])-30:len(e.time[0])]
        else:
            timeE = e.time[0]
        date = datetime.date.today()
        time = datetime.datetime.now().time()
        if (len(e.clubname[0])>30):
            org = e.clubname[0][len(e.clubname[0])-30:len(e.clubname[0])]
        else:
            org = e.clubname[0]

        #Need to come up with topic for Org
        try:
            orgPrime = Organization.objects.get(name=org)
        except Organization.DoesNotExist as e:
            orgPrime = Organization()
            orgPrime.name = org

        m = Event()
        m.name = name
        m.location = location
        print(location)
        m.date = date
        m.time = time
        #m.dateE = dateE
        #m.timeE = timeE
        #m.organization = orgPrime
        #m.img_url = url
        m.save()
