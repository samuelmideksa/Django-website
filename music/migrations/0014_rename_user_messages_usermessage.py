# Generated by Django 5.0.2 on 2024-02-26 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_rename_album_artist_album_artists'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Messages',
            new_name='UserMessage',
        ),
    ]
