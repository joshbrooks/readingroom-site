# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0006_homepagecarouselitem")]

    operations = [
        migrations.AddField(
            model_name="homepagecarouselitem",
            name="description",
            field=models.TextField(blank=True),
        )
    ]
