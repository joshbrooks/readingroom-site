# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-15 19:16
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [("home", "0039_auto_20180201_0931")]

    operations = [
        migrations.RenameField(
            model_name="eventindexpage", old_name="intro", new_name="intro_en"
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="intro_tet",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]