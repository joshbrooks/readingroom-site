# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0032_add_bulk_delete_page_permission"),
        ("home", "0022_auto_20170304_1539"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberShipPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("telephone", models.CharField(blank=True, max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("address_1", models.CharField(blank=True, max_length=255)),
                ("address_2", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(blank=True, max_length=255)),
                ("country", models.CharField(blank=True, max_length=255)),
                ("post_code", models.CharField(blank=True, max_length=10)),
                ("intro", wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ("body", wagtail.wagtailcore.fields.RichTextField(blank=True)),
                (
                    "thank_you_text",
                    wagtail.wagtailcore.fields.RichTextField(blank=True),
                ),
                (
                    "to_address",
                    models.CharField(
                        blank=True,
                        help_text="Optional - form submissions will be emailed to this address",
                        max_length=255,
                    ),
                ),
                ("from_address", models.CharField(blank=True, max_length=255)),
                ("subject", models.CharField(blank=True, max_length=255)),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="MembershipRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=255, verbose_name="Email Address"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Phone Number"
                    ),
                ),
                ("message", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SpaceRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("organisation", models.CharField(blank=True, max_length=255)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=255, verbose_name="Email Address"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Phone Number"
                    ),
                ),
                (
                    "preffered",
                    models.TextField(
                        blank=True, null=True, verbose_name="Prefered Form of Contact"
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        blank=True, null=True, verbose_name="Body of Inquiry"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="bookspace",
            name="from_address",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="bookspace",
            name="subject",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="bookspace",
            name="thank_you_text",
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="bookspace",
            name="to_address",
            field=models.CharField(
                blank=True,
                help_text="Optional - form submissions will be emailed to this address",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="organisation",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="contactmessage",
            name="preffered",
            field=models.TextField(
                blank=True, null=True, verbose_name="Prefered Form of Contact"
            ),
        ),
        migrations.AlterField(
            model_name="contactmessage",
            name="message",
            field=models.TextField(blank=True, null=True, verbose_name="Message"),
        ),
    ]
