# Generated by Django 2.2.9 on 2020-01-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200121_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'resume categories',
            },
        ),
    ]
