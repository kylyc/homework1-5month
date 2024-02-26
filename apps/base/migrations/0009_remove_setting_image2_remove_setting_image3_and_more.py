# Generated by Django 4.2.10 on 2024-02-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_setting_image2_setting_image3_setting_image4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='image4',
        ),
        migrations.AddField(
            model_name='setting',
            name='title2',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]