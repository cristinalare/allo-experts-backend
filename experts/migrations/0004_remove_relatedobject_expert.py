# Generated by Django 5.1.2 on 2024-11-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0003_remove_expert_content_type_remove_expert_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedobject',
            name='expert',
        ),
    ]
