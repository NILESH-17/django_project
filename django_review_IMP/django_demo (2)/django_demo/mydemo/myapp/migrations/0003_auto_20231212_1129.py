# Generated by Django 2.2 on 2023-12-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_review_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
