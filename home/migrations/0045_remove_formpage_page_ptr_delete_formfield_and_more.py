# Generated by Django 4.2.6 on 2023-11-20 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_formpage_formfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
