# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailforms", "0003_capitalizeverbose"),
        ("wagtailcore", "0032_add_bulk_delete_page_permission"),
        ("wagtailredirects", "0005_capitalizeverbose"),
        ("home", "0011_auto_20170121_1515"),
    ]

    operations = [
        migrations.RemoveField(model_name="eventspage", name="page_ptr"),
        migrations.RemoveField(model_name="eventspagecarouselitem", name="image"),
        migrations.RemoveField(
            model_name="eventspagecarouselitem", name="link_document"
        ),
        migrations.RemoveField(model_name="eventspagecarouselitem", name="link_page"),
        migrations.RemoveField(model_name="eventspagecarouselitem", name="page"),
        migrations.DeleteModel(name="EventsPage"),
        migrations.DeleteModel(name="EventsPageCarouselItem"),
    ]
