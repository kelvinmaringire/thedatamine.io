# Generated by Django 4.2.6 on 2023-11-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepage_about_href_homepage_about_list_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_href_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
