"""Migration to update ArticleTag field lengths.

Changes:
- Increase max_length of ArticleTag.name from 50 to 100
- Increase max_length of ArticleTag.slug from 50 to 100
"""

# Generated by Django 3.1.2 on 2020-11-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration class for updating ArticleTag field lengths."""

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
