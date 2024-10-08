from django.conf import settings
from django.db import models

from users.models import CustomUser


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'topic'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['name']


class Article(models.Model):
    class Status(models.TextChoices):
        pending = 'Pending', 'Pending'
        publish = 'Publish', 'Publish'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.pending)
    thumbnail = models.ImageField(upload_to="articles/%Y/%m/%d")
    topics = models.ManyToManyField(Topic)
    views_count = models.IntegerField(default=0)
    reads_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_at']


class Clap(models.Model):
    article = models.ForeignKey(Article, related_name='claps', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('article', 'user')

    def __str__(self):
        return f'{self.user} clapped {self.count} times for {self.article}'
