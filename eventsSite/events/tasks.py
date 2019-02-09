from __future__ import absolute_import, unicode_literals
from celery import shared_task
from converter import *

@shared_task
def gather_data():
    return retrieve()
