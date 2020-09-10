# Generated by Django 2.2.9 on 2020-01-25 00:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0014_resumepageskill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumepageskill',
            name='icons',
        ),
        migrations.CreateModel(
            name='ResumePageSkillIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.ResumePageSkill')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_resumepageskillicon_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='resumepageskill',
            name='icons',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.ResumePageSkillIcon', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]