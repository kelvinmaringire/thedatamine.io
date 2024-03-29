# Generated by Django 4.2.6 on 2023-10-17 10:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0005_rename_navigation_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_button_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_button_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_subtitle',
            field=wagtail.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
