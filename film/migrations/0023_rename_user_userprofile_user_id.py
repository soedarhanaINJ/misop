# Generated by Django 4.2.4 on 2023-09-28 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0022_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_id',
        ),
    ]