# Generated by Django 3.2.6 on 2021-09-14 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkedit_app', '0002_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='file',
            new_name='url',
        ),
    ]
