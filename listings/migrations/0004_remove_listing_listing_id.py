# Generated by Django 2.2 on 2019-07-30 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_listing_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listing_id',
        ),
    ]
