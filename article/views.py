from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from article.models import Article
from article.文章表格 import ArticleForm
from django.shortcuts import get_object_or_404

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
			# Process the data in form.cleaned_data
			# ...
#			Article(form)
			return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		a=Article.objects.get(pk=2886)
		form = ArticleForm(request.POST, instance=a) # An unbound form
#		form = ArticleForm(a) # An unbound form
#		print(form.title)
#		form.title='@@'
		print(form)
		print(a)

	return render(request, 'article/edit.html', {
		'form': form,
	})
# Create your views here.
def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

class Results(generic.DetailView):
	model=Article
	template_name = 'article/resultz.html'

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)