# Generated by Django 2.2.9 on 2020-03-26 21:10

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200326_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeother',
            name='desc',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resumeother',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
