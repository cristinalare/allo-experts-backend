# Generated by Django 5.1.2 on 2024-11-20 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Categories'},
        ),
    ]