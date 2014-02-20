from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from article.models import Article
from article.文章表格 import 文章全部表格
from article.文章表格 import 加新文章表格, 改國語斷詞表格, 改閩南語翻譯表格
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect

def index(request):
	latest_poll_list = Article.objects.order_by('-date')[:50]
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))

class 看文章(generic.DetailView):
	model = Article
	template_name = 'article/看文章.html'

def 加新文章(request):
	if request.method == 'POST':  # If the form has been submitted...
		form = 文章全部表格(request.POST)  # A form bound to the POST data
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/article/')  # Redirect after POST
	return render(request, 'article/新文章.html', {
		'article': 加新文章表格(),
	})

def 全改(request, pk):
	return 編輯(request, pk, 'article/全改.html', 文章全部表格)
def 改國語斷詞(request, pk):
	return 編輯(request, pk, 'article/改國語斷詞.html', 改國語斷詞表格)
def 改閩南語翻譯(request, pk):
	return 編輯(request, pk, 'article/改閩南語翻譯.html', 改閩南語翻譯表格)
	
def 編輯(request, pk, 網址, 表格):
	if request.method == 'POST':  # If the form has been submitted...
		article = Article.objects.get(pk=pk)
		form = 表格(request.POST, instance=article)
		if form.is_valid():  # All validation rules pass
			form.save()
			return HttpResponseRedirect('/article/')  # Redirect after POST
	article = Article.objects.get(pk=pk)
	form = 表格(instance=article)

	return render(request, 網址, {
		'article': form,
	})
# 無法度用form＠＠
class EditView(generic.DetailView):
	model = Article
	form_class = 文章全部表格
	template_name = 'article/改.html'
