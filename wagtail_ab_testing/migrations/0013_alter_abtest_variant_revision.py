# Generated by Django 4.1.13 on 2023-11-28 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("wagtail_ab_testing", "0001_squashed_0012_abtest_variant_revision"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abtest",
            name="variant_revision",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.revision",
            ),
        ),
    ]
