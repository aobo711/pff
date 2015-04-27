# -*- coding: utf-8 -*-
from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib.djangoitem import DjangoItem



class Game(models.Model):
    name = models.CharField(max_length=200)

    icon = models.ImageField()

    packageName = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    parent = models.ForeignKey('self', null=True, blank=True)

    thumbnail = models.ImageField()

    description = models.TextField(null=True)

    game = models.ForeignKey(Game)

    def __unicode__(self):
        return self.name



class Source(models.Model):
    name = models.CharField(max_length=200)

    thumbnail = models.ImageField(upload_to='images/source/', null=True, blank=True)

    description = models.TextField(null=True)

    type_chieces = (
        ('pc_web', '网站'),
        ('mobile_web', '移动网站'),
        ('app', '应用'),
    )

    game = models.ForeignKey(Game)
    
    type = models.CharField(max_length=20, choices=type_chieces, default='pc_web', null=True, blank=True)

    status_chieces = (
        ('0', 'inactived'),
        ('1', 'actived')
    )

    status = models.CharField(max_length=20, choices=status_chieces, default='1', null=True, blank=True)

    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200)

    summary = models.TextField()

    content = models.TextField()

    author = models.CharField(max_length=50)

    source = models.ForeignKey(Source)

    created_at = models.DateTimeField(blank=True,null=True)

    crawled_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(blank=True,null=True)

    first_video = models.CharField(max_length=200,blank=True,null=True)

    categories = models.ManyToManyField(Category,null=True,blank=True)

    thumbnail = models.CharField(max_length=200,blank=True,null=True)

    STAUTS_CHOICE = (
        ('-1', '× 弃用'),
        ('1', '√ 已审核'),
        ('0', '? 尚未审核'),
    )

    status = models.CharField(max_length=2, default='1', choices=STAUTS_CHOICE, null=True, blank=True)

    url = models.URLField()

    game = models.ForeignKey(Game)

    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title


class ArticleItem(DjangoItem):
    django_model = Article

