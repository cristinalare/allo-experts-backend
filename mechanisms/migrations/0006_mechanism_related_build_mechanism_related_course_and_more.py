# Generated by Django 5.1.2 on 2024-11-01 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0003_build_metadata_build_status_build_type'),
        ('courses', '0001_initial'),
        ('experts', '0001_initial'),
        ('mechanisms', '0005_alter_mechanism_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanism',
            name='related_build',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='builds.build'),
        ),
        migrations.AddField(
            model_name='mechanism',
            name='related_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course'),
        ),
        migrations.AddField(
            model_name='mechanism',
            name='related_expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='experts.expert'),
        ),
    ]
