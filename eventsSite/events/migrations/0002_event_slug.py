# Generated by Django 2.1.5 on 2019-02-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]