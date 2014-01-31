from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from article.models import Article

def index(request):
    latest_poll_list = Article.objects.order_by('date')[:5]
#    output = ', '.join([p.title for p in latest_poll_list])
#    return HttpResponse(output)
    template = loader.get_template('article/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))


# Create your views here.
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)