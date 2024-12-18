# Generated by Django 5.1.1 on 2024-10-31 21:27

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('expert_in', models.CharField(choices=[('allo_Experts', 'Allo Experts'), ('allo_dev', 'Allo Dev')], default='allo_Experts', max_length=40)),
                ('contact_info_telegram', models.CharField(max_length=50)),
                ('contact_info_twitter', models.CharField(max_length=50)),
                ('contact_info_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='RelatedObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
