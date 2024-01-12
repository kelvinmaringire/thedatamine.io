# Generated by Django 4.2.6 on 2023-10-16 20:30

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_navigation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='navigation',
            field=wagtail.fields.StreamField([('navigation', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock())]))], null=True, use_json_field=True),
        ),
    ]