# Generated by Django 4.2.6 on 2023-10-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_homepage_body_homepage_hero_button_page_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_button_page_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_button_url_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
