# Generated by Django 2.2.9 on 2020-01-25 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('blog', '0013_auto_20200125_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumePageSkill',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('head', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
                ('icons', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
