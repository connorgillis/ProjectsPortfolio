# Generated by Django 2.2.9 on 2020-01-21 01:13

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_resumecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumepageitem',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.ResumeCategory'),
        ),
    ]
