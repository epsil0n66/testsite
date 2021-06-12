from django.db import models
import datetime

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('содержание статьи')
    pub_date = models.DateField('время публикации статьи')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 10)
    comment_text = models.CharField('текст комментария', max_length = 500)
    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'