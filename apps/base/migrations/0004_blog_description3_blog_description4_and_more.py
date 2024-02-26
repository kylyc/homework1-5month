# Generated by Django 4.2.10 on 2024-02-26 07:03

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_blog_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description3',
            field=models.TextField(default=1, max_length=500, verbose_name='Описание3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description4',
            field=models.TextField(default=1, max_length=500, verbose_name='Описание4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description5',
            field=models.TextField(default=1, max_length=500, verbose_name='Описание5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='description6',
            field=models.TextField(default=1, max_length=500, verbose_name='Описание5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=django_resized.forms.ResizedImageField(crop=None, default=1, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image3',
            field=django_resized.forms.ResizedImageField(crop=None, default=1, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image4',
            field=django_resized.forms.ResizedImageField(crop=None, default=1, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image5',
            field=django_resized.forms.ResizedImageField(crop=None, default=1, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title3',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title4',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок3'),
            preserve_default=False,
        ),
    ]
