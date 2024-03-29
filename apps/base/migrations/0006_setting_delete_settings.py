# Generated by Django 4.2.10 on 2024-02-26 07:46

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_blog_description7_blog_title5_blog_title6_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('dribbble', models.URLField(blank=True, max_length=255, null=True, verbose_name='dribble')),
                ('youtube', models.URLField(blank=True, max_length=255, null=True, verbose_name='youtube')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='image/')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта ',
            },
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
