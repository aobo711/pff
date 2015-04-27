from django.contrib import admin
from django.conf import settings
from django_scraper.models import Source, Article, Category, Game

class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'status', 'scraper')
    list_display_links = ('name',)
    list_editable = ('status',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'thumbnail_', 'game_')
    list_display_links = ('name',)
    
    def thumbnail_(self, instance):
        return '<img src="%s" width="68" />' % (instance.thumbnail.url)
    thumbnail_.allow_tags = True

    def game_(self, instance):
        return '<a href="../game/%s" />%s</a>' % ( instance.game.id, instance.game.name)
    game_.allow_tags = True


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_', 'packageName')
    list_display_links = ('name',)

    def icon_(self, instance):
        return '<img src="%s" />' % (instance.icon.url)
    icon_.allow_tags = True

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'source_', 'crawled_at')
    list_display_links = ('title',)
    list_filter = ('source',)

    ordering = ['-created_at']
    
    def source_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.source.name)
    source_.allow_tags = True


admin.site.register(Source, SourceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)