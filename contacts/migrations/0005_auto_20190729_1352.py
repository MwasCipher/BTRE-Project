# Generated by Django 2.2 on 2019-07-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20190729_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.CharField(max_length=100),
        ),
    ]
