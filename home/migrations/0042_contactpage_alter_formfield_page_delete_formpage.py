# Generated by Django 4.2.6 on 2023-11-20 22:34

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.forms.models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0041_rename_form_page_formfield_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('subtitle', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.contactpage'),
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]