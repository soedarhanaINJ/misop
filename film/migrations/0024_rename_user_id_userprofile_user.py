# Generated by Django 4.2.4 on 2023-09-28 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0023_rename_user_userprofile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_id',
            new_name='user',
        ),
    ]
