import os
import processors

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pff.settings") #Changed in DDS v.0.3

BOT_NAME = 'PFF'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'django_scraper.scraper',]

CUSTOM_PROCESSORS = 'django_scraper.scraper.processors'

# USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')
USER_AGENT = 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; Nexus-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'dynamic_scraper.pipelines.DjangoImagesPipeline',
    'django_scraper.scraper.pipelines.DjangoWriterPipeline',
]

IMAGES_STORE = os.path.join(PROJECT_ROOT, '../thumbnails')

IMAGES_THUMBS = {
    'small': (170, 170),
}