# Generated by Django 5.0.2 on 2024-02-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
    ]
