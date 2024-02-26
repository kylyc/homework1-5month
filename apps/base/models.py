from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Settings(models.Model):
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    dribbble = models.URLField(
        max_length=255,
        verbose_name='dribble',
        blank=True, null=True
    )
    youtube = models.URLField(
        max_length=255,
        verbose_name='youtube',
        blank=True, null=True
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    title3 = models.CharField(
        max_length=255,
        verbose_name="Загловок2"
    )
    description2 = models.TextField(
        verbose_name="Описание"
    )
    image2 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image3 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image4 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image5 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image6 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image7 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image8 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    image9 = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    title4 = models.CharField(
        max_length=255,
        verbose_name="Загловок2"
    )
    description3 = models.TextField(
        verbose_name="Описание"
    )
    title5 = models.CharField(
        max_length=255,
        verbose_name="Загловок2"
    )
    description4 = models.TextField(
        verbose_name="Описание"
    )
    title6 = models.CharField(
        max_length=255,
        verbose_name="Загловок2"
    )
    description5 = models.TextField(
        verbose_name="Описание"
    )
    title7 = models.CharField(
        max_length=255,
        verbose_name="Загловок2"
    )
    description6 = models.TextField(
        verbose_name="Описание"
    )
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта "



class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок новости"
    )
    descriptions = models.TextField(
        verbose_name="Описание новости"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    create = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания новости",
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    image = ResizedImageField(
        force_format="WEBP",
	    quality=100,
        upload_to="image/"
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание"
    )
    description2 = models.TextField(
        max_length=500,
        verbose_name="Описание2"
    )
    image2 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to="image/"
    )
    image3 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to="image/"
    )
    image4 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to="image/"
    )
    image5 = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to="image/"
    )
    description3 = models.TextField(
        max_length=500,
        verbose_name="Описание3"
    )
    description4 = models.TextField(
        max_length=500,
        verbose_name="Описание4"
    )
    title3 = models.CharField(
        max_length=255,
        verbose_name="Заголовок2"
    )
    title4 = models.CharField(
        max_length=255,
        verbose_name="Заголовок3"
    )
    description5 = models.TextField(
        max_length=500,
        verbose_name="Описание5"
    )
    description6 = models.TextField(
        max_length=500,
        verbose_name="Описание6"
    )
    title5 = models.CharField(
        max_length=255,
        verbose_name="Заголовок4"
    )
    title6 = models.CharField(
        max_length=255,
        verbose_name="Заголовок5"
    )
    description7 = models.TextField(
        max_length=500,
        verbose_name="Описание7"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"