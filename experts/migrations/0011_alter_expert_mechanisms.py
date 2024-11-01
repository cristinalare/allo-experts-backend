# Generated by Django 5.1.2 on 2024-11-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0010_delete_relatedobject'),
        ('mechanisms', '0007_remove_mechanism_related_build_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='mechanisms',
            field=models.ManyToManyField(blank=True, related_name='related_experts', to='mechanisms.mechanism'),
        ),
    ]