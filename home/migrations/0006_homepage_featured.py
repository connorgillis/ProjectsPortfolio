# Generated by Django 2.2.9 on 2020-02-15 00:45

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200210_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
