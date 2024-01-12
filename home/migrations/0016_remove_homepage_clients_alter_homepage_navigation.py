# Generated by Django 4.2.6 on 2023-11-01 22:05

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_homepage_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='clients',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='navigation',
            field=wagtail.fields.StreamField([('navigation', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock()), ('show', wagtail.blocks.BooleanBlock(default=True, required=False))]))], null=True, use_json_field=True),
        ),
    ]