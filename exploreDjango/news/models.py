from django.db import models


# Create your models here.
class Arctiles(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anounce = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'