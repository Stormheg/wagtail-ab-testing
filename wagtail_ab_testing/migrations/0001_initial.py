# Generated by Django 3.1.3 on 2020-11-03 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0052_pagelogentry"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbTest",
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
                ("name", models.CharField(max_length=255)),
                ("goal_event", models.CharField(max_length=255)),
                ("sample_size", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("running", "Running"),
                            ("paused", "Paused"),
                            ("cancelled", "Cancelled"),
                            ("completed", "Completed"),
                        ],
                        default="draft",
                        max_length=20,
                    ),
                ),
                (
                    "goal_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ab_tests",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "treatment_revision",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.pagerevision",
                    ),
                ),
            ],
        ),
    ]
