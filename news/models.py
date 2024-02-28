from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    is_published = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    name_category = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    