# Generated by Django 4.2.6 on 2023-11-03 23:59

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_homepage_portfolio_homepage_portfolio_subtitle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='portfolio',
            field=wagtail.fields.StreamField([('portfolio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('category', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('details_url', wagtail.blocks.URLBlock(required=False))]))], null=True, use_json_field=True),
        ),
    ]
