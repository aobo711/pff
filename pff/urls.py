from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from pff import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/sources/$', views.source),
    url(r'^v1/news/$', views.listing),
    # url(r'^v1/news/(\d+)$', views.news_detail),
    url(r'^v1/feedback/', views.feedback),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
