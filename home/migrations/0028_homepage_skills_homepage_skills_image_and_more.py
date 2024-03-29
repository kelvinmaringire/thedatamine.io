# Generated by Django 4.2.6 on 2023-11-02 22:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0027_homepage_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='skills',
            field=wagtail.fields.StreamField([('skill', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock()), ('show', wagtail.blocks.BooleanBlock(default=True, required=False))]))], null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skills_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skills_subtitle',
            field=wagtail.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skills_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
