# Generated by Django 4.2.6 on 2023-11-01 08:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('navigation', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock()), ('show', wagtail.blocks.BooleanBlock(blank=True, default=True, null=True))]))], null=True, use_json_field=True),
        ),
    ]