# -*- coding: UTF-8 -*-   
from django.db.utils import IntegrityError
import lxml.html, re
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from django_scraper.models import Game, Category

class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        try:
            item['source'] = spider.ref_object

            # checker_rt = SchedulerRuntime(runtime_type='C')
            # checker_rt.save()
            # item['checker_runtime'] = checker_rt
            game_meta = spider.ref_object.name.split('-')

            item['game'] = Game.objects.get(name=item['source'].game.name)

            # remove ad
            content = re.sub(r'<script([\s\S]*)</script>', '', item['content'])
            # remove jiathis codes
            content = re.sub(r'<!-- JiaThis Button BEGIN -->([\s\S]*)<!-- JiaThis Button END -->', '', content)
            # remove style
            content = re.sub(r'style=".*?"', '', content)

            item['content'] = content
            
            if 'summary' not in item.keys():
                # generate summary
                t = lxml.html.fromstring(content)

                content = t.text_content().replace('\n', ' ').replace('\r', '')
                content = re.sub(r'\s+', '', content)
                item['summary'] = content[:50]

            item = item.save()

            article_category = game_meta[1]
            item.categories.add(Category.objects.get(name=article_category.strip()))

            spider.action_successful = True
            spider.log("Item saved.", log.INFO)

        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")

        return item