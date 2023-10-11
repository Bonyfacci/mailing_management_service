from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    photo = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Фото')
    created_date = models.DateTimeField(**NULLABLE, verbose_name='Дата публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title} {self.content}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('created_date', )
