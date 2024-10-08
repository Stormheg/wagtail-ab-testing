# Generated by Django 3.1.3 on 2020-11-05 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_ab_testing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbTestHourlyLog",
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
                    "variant",
                    models.CharField(
                        choices=[("control", "Control"), ("treatment", "Treatment")],
                        max_length=9,
                    ),
                ),
                ("date", models.DateField()),
                ("hour", models.PositiveSmallIntegerField()),
                ("participants", models.PositiveIntegerField(default=0)),
                ("conversions", models.PositiveIntegerField(default=0)),
                (
                    "ab_test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hourly_logs",
                        to="wagtail_ab_testing.abtest",
                    ),
                ),
            ],
            options={
                "ordering": ["ab_test", "variant", "date", "hour"],
                "unique_together": {("ab_test", "variant", "date", "hour")},
            },
        ),
    ]
