# Generated by Django 3.2.3 on 2021-05-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='usernames',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_1',
            field=models.TextField(blank=True),
        ),
    ]