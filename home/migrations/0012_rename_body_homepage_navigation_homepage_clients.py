# Generated by Django 4.2.6 on 2023-11-01 21:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='navigation',
        ),
        migrations.AddField(
            model_name='homepage',
            name='clients',
            field=wagtail.fields.StreamField([('clients', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], null=True, use_json_field=True),
        ),
    ]