# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-15 19:53
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [("home", "0042_auto_20180415_1941")]

    operations = [
        migrations.AddField(
            model_name="eventpage",
            name="intro_en",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="eventpage",
            name="intro_tet",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
