# Generated by Django 4.2.6 on 2023-11-03 23:41

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_homepage_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='portfolio',
            field=wagtail.fields.StreamField([('portfolio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('category', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_alt', wagtail.blocks.CharBlock(required=False)), ('lightbox_title', wagtail.blocks.CharBlock()), ('details_url', wagtail.blocks.URLBlock(required=False))]))], null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='portfolio_subtitle',
            field=wagtail.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='portfolio_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
