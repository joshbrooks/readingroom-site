# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-22 10:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [("home", "0035_auto_20180122_1025")]

    operations = [
        migrations.RenameField(
            model_name="permanentexhibitionindex", old_name="body", new_name="body_en"
        ),
        migrations.RenameField(
            model_name="permanentexhibitionindex", old_name="intro", new_name="intro_en"
        ),
        migrations.AddField(
            model_name="permanentexhibitionindex",
            name="body_tet",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="permanentexhibitionindex",
            name="intro_tet",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
