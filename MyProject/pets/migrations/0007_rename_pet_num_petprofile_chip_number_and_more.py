# Generated by Django 4.1 on 2022-12-15 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_petprofile_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petprofile',
            old_name='pet_num',
            new_name='chip_number',
        ),
        migrations.RenameField(
            model_name='petprofile',
            old_name='pet_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='petprofile',
            old_name='pet_sex',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='petprofile',
            old_name='pet_image',
            new_name='image',
        ),
    ]
