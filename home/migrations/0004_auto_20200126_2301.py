# Generated by Django 2.2.9 on 2020-01-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sec1',
            field=models.CharField(default='lorem', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='sec2',
            field=models.CharField(default='lorem', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='sec3',
            field=models.CharField(default='lorem', max_length=250),
            preserve_default=False,
        ),
    ]