# Generated by Django 4.2.10 on 2024-02-26 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_setting_delete_settings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='descriptions',
            new_name='description',
        ),
    ]
