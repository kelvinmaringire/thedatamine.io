# Generated by Django 4.2.6 on 2023-11-02 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_homepage_why_us_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='why_us_accordion',
        ),
    ]
