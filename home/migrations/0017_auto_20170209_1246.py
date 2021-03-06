# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtaildocs", "0007_merge"),
        ("wagtailcore", "0032_add_bulk_delete_page_permission"),
        ("home", "0016_remove_homepage_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutPageBlocks",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "link_external",
                    models.URLField(blank=True, verbose_name="External link"),
                ),
                ("title", models.CharField(help_text="Title", max_length=255)),
                ("body", wagtail.wagtailcore.fields.RichTextField(blank=True)),
                (
                    "link_title",
                    models.CharField(help_text="Link title", max_length=255),
                ),
                (
                    "link_document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtaildocs.Document",
                    ),
                ),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_blocks",
                        to="home.AboutPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
        migrations.CreateModel(
            name="LibraryPageBlocks",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "link_external",
                    models.URLField(blank=True, verbose_name="External link"),
                ),
                ("title", models.CharField(help_text="Title", max_length=255)),
                ("body", wagtail.wagtailcore.fields.RichTextField(blank=True)),
                (
                    "link_title",
                    models.CharField(help_text="Link title", max_length=255),
                ),
                (
                    "link_document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtaildocs.Document",
                    ),
                ),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_blocks",
                        to="home.LibraryPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
        migrations.CreateModel(
            name="MuseumPageBlocks",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "link_external",
                    models.URLField(blank=True, verbose_name="External link"),
                ),
                ("title", models.CharField(help_text="Title", max_length=255)),
                ("body", wagtail.wagtailcore.fields.RichTextField(blank=True)),
                (
                    "link_title",
                    models.CharField(help_text="Link title", max_length=255),
                ),
                (
                    "link_document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtaildocs.Document",
                    ),
                ),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_blocks",
                        to="home.MuseumPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
        migrations.RenameModel(
            old_name="BoardOfGoverners", new_name="BoardOfGovernors"
        ),
        migrations.RenameModel(
            old_name="BoardOfGovernersCarouselItem",
            new_name="BoardOfGovernorsCarouselItem",
        ),
    ]
