# Generated by Django 4.1.4 on 2022-12-21 04:38

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile/profile.jpg', max_length=255, null=True, upload_to=account.models.get_profile_image_filepath),
        ),
    ]
