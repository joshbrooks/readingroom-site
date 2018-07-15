# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0017_reduce_focal_point_key_max_length"),
        ("home", "0027_auto_20170327_1615"),
    ]

    operations = [
        migrations.RemoveField(model_name="membershiprequest", name="message"),
        migrations.AddField(
            model_name="exhibitionpage",
            name="cost",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="date_from",
            field=models.DateField(blank=True, null=True, verbose_name="Start date"),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="date_to",
            field=models.DateField(
                blank=True,
                help_text="Not required if event is on a single day",
                null=True,
                verbose_name="End date",
            ),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="feed_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.Image",
            ),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="location",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="time_from",
            field=models.TimeField(blank=True, null=True, verbose_name="Start time"),
        ),
        migrations.AddField(
            model_name="exhibitionpage",
            name="time_to",
            field=models.TimeField(blank=True, null=True, verbose_name="End time"),
        ),
    ]
