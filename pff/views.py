import json,re
from BeautifulSoup import BeautifulSoup
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,HttpResponseBadRequest
from django_scraper.models import Article, Source
from django.db.models import Q
import lxml.html

def generate_q(request, tag):
    q = Q(status=1)
    return q


def fetch_news(request, tag):
    count = request.GET.get('max', 10)
    start = request.GET.get('start', 0)
    refresh = request.GET.get('refresh', 0)
    end = int(start) + int(count)

    if refresh == 1:
        start = 0
        end = 10
    
    result_list = Article.objects.filter(generate_q(request, tag)).order_by('-created_at')[start:end]

    for item in result_list:
        content = item.content
        t = lxml.html.fromstring(content)
        
        soup = BeautifulSoup(content)
        images = soup.findAll('img')
        thumbnail = ''
        if images:
            thumbnail = soup.findAll('img')[0]['src']
        
        if thumbnail.find('//') == 0:
            thumbnail = 'http:' + thumbnail

        content = t.text_content().replace('\n', ' ').replace('\r', '')
        content = re.sub(r'\s+', '', content)
        item.content = content[:100]
        item.thumbnail = thumbnail

    return result_list

def listing(request):
    result_list = fetch_news(request, '')
    context = {'news': result_list}
    render = render_to_string('news.json', context)
    return HttpResponse(render,content_type='application/json;charset=utf-8')

def source(request):
    result_list = Source.objects.filter(Q(scraper__status='A'))
    context = {'sources': result_list}
    render = render_to_string('source.json', context)
    return HttpResponse(render,content_type='application/json;charset=utf-8')

# receive feedback post
@csrf_exempt
def feedback(request):
    desc = request.POST.get('desc', '')
    if not desc:
        return HttpResponseBadRequest('Missing desc.')

    contact = request.POST.get('contact', '')
    udid = request.POST.get('udid', '')
    os_version = request.POST.get('os_version', '')
    api_level = request.POST.get('api_level', '')
    device = request.POST.get('device', '')
    model = request.POST.get('model', '')

    feedback = Feedback.create(desc)
    feedback.contact = contact;
    feedback.udid = udid;
    feedback.os_version = os_version
    feedback.api_level = api_level
    feedback.device = device
    feedback.model = model

    feedback.save()

    return JsonResponse({
            'message' : 'Feedback Received.'
        })
