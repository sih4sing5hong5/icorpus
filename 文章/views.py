from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from 文章.models import 何澤政文章
from 文章.文章表格 import 文章全部表格
from 文章.文章表格 import 加新文章表格, 改國語斷詞表格, 改閩南語翻譯表格
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect

def index(request):
	latest_poll_list = 何澤政文章.objects.order_by('-pk')[:50]
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('文章/全部文章.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))

class 看文章(generic.DetailView):
	model = 何澤政文章
	template_name = '文章/看文章.html'

def 加新文章(request):
	if request.method == 'POST':  # If the form has been submitted...
		文章表格 = 加新文章表格(request.POST)  # A form bound to the POST data
		if 文章表格.is_valid():
			文章表格.save()
			return HttpResponseRedirect('/文章/')  # Redirect after POST
	else:
		文章表格=加新文章表格()
	return render(request, '文章/新文章.html', {
		'文章': 文章表格,
	})

def 全改(request, pk):
	return 編輯(request, pk, '文章/全改.html', 文章全部表格)
def 改分類佮原文(request, pk):
	return 編輯(request, pk, '文章/新文章.html', 加新文章表格)
def 改國語斷詞(request, pk):
	return 編輯(request, pk, '文章/改國語斷詞.html', 改國語斷詞表格)
def 改閩南語翻譯(request, pk):
	return 編輯(request, pk, '文章/改閩南語翻譯.html', 改閩南語翻譯表格)
	
def 編輯(request, pk, 網址, 表格):
	if request.method == 'POST':  # If the form has been submitted...
		文章 = 何澤政文章.objects.get(pk=pk)
		form = 表格(request.POST, instance=文章)
		if form.is_valid():  # All validation rules pass
			form.save()
			return HttpResponseRedirect('/文章/')  # Redirect after POST
	else:
		文章 = 何澤政文章.objects.get(pk=pk)
		form = 表格(instance=文章)
	
	return render(request, 網址, {
		'文章': form,
	})
# 無法度用form＠＠
class EditView(generic.DetailView):
	model = 何澤政文章
	form_class = 文章全部表格
	template_name = '文章/改.html'
