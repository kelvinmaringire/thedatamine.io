# Generated by Django 4.2.6 on 2023-11-18 09:41

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_homepage_faq_homepage_faq_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_map',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_subtitle',
            field=wagtail.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='contact_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
