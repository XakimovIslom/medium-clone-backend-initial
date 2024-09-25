from django.contrib import admin

from articles.models import Article, Topic, Clap

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Clap)