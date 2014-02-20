from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from article.models import Article
from article.文章表格 import ArticleForm
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect

def index(request):
	latest_poll_list = Article.objects.order_by('-date')[:50]
#	output = ', '.join([p.title for p in latest_poll_list])
#	return HttpResponse(output)
	template = loader.get_template('article/index.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))

def edit(request,pk):
	if request.method == 'POST': # If the form has been submitted...
		form = ArticleForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			article = Article.objects.get(pk=pk)
			form = ArticleForm(request.POST, instance = article)
			form.save()
# 			return redirect('/')
			# Process the data in form.cleaned_data
			# ...
#			Article(form)
			return HttpResponseRedirect('/article/') # Redirect after POST
	article=Article.objects.get(pk=pk)
	form = ArticleForm(instance=article)

	return render(request, 'article/改.html', {
		'article': form,
	})
# 無法度用form＠＠
class EditView(generic.DetailView):
	model = Article
	form_class = ArticleForm
	template_name = 'article/改.html'

class Results(generic.DetailView):
	model=Article
	template_name = 'article/看.html'
