# Generated by Django 2.2.9 on 2020-02-01 20:16

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_formfield_formpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepageitem',
            name='desc',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
