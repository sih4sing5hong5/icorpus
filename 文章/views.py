from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from 文章.models import 何澤政文章
from 文章.文章表格 import 文章全部表格
from 文章.文章表格 import 加新文章表格, 改國語斷詞表格, 改閩南語翻譯表格
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.base import View
from 文章.斷詞翻譯 import 斷詞
from 文章.斷詞翻譯 import 翻譯


def index(request):
    揣著文章 = 何澤政文章.objects.order_by('-pk')
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
    template = loader.get_template('文章/全部文章.html')
    context = RequestContext(request, {
        '揣著文章': 揣著文章[:20],
        '有登入無': request.user.is_authenticated(),
    })
    return HttpResponse(template.render(context))


def 全部文章(request):
    揣著文章 = 何澤政文章.objects.order_by('-pk')
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
    template = loader.get_template('文章/全部文章.html')
    context = RequestContext(request, {
        '揣著文章': 揣著文章,
        '有登入無': request.user.is_authenticated(),
    })
    return HttpResponse(template.render(context))


def 揣文章(request):
    try:
        字串 = request.POST['揣'].strip()
    except:
        字串 = ''
    無減號字串 = 字串.replace('-', '')
    揣著文章 = 何澤政文章.objects.filter(
        Q(原本標題__contains=字串) |
        Q(原本內容__contains=字串) |
        Q(斷詞標題__contains=字串) |
        Q(斷詞內容__contains=字串) |
        Q(教羅標題__contains=字串) |
        Q(教羅內容__contains=字串) |
        Q(原本標題__contains=無減號字串) |
        Q(原本內容__contains=無減號字串) |
        Q(斷詞標題__contains=無減號字串) |
        Q(斷詞內容__contains=無減號字串) |
        Q(教羅標題__contains=無減號字串) |
        Q(教羅內容__contains=無減號字串)
    ).order_by('-pk')
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
    template = loader.get_template('文章/全部文章.html')
    context = RequestContext(request, {
        '揣著文章': 揣著文章,
        '有登入無': request.user.is_authenticated(),
    })
    return HttpResponse(template.render(context))


def 看文章(request, pk):
    揣著文章 = 何澤政文章.objects.get(pk=pk)
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
    template = loader.get_template('文章/看文章.html')
    context = RequestContext(request, {
        '何澤政文章': 揣著文章,
        '有登入無': request.user.is_authenticated(),
    })
    return HttpResponse(template.render(context))
# class 登入物件(object):
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(登入物件, self).dispatch(*args, **kwargs)

# class 看文章(generic.DetailView):
# # class 看文章(登入物件,generic.DetailView):
# 	model = 何澤政文章
# 	template_name = '文章/看文章.html'


@login_required(login_url='/登入/')
def 加新文章(request):
    if request.method == 'POST':  # If the form has been submitted...
        文章表格 = 加新文章表格(request.POST)  # A form bound to the POST data
        if 何澤政文章.這標題有用過無(request.POST['原本標題']):
            return render(request, '文章/新聞標題用過矣.html', {
                '原本標題': request.POST['原本標題']
            })
        if 文章表格.is_valid():
            文章 = 文章表格.save()
            文章.自動斷詞()
            return redirect('改國語斷詞', pk=文章.pk)
    else:
        文章表格 = 加新文章表格()
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


@login_required(login_url='/登入/')
def 編輯(request, pk, 網址, 表格):
    if request.method == 'POST':  # If the form has been submitted...
        文章 = 何澤政文章.objects.get(pk=pk)
        form = 表格(request.POST, instance=文章)
        if form.is_valid():  # All validation rules pass
            文章 = form.save()
            if 網址 == '文章/新文章.html':
                文章.自動斷詞()
                return redirect('改國語斷詞', pk=pk)
            if 網址 == '文章/改國語斷詞.html':
                文章.自動翻譯()
                return redirect('改閩南語翻譯', pk=pk)
            if 網址 == '文章/改閩南語翻譯.html':
                return redirect('看文章', pk=pk)
            return redirect('首頁')
    else:
        文章 = 何澤政文章.objects.get(pk=pk)
        form = 表格(instance=文章)

    return render(request, 網址, {
        '文章': form,
        '有登入無': request.user.is_authenticated(),
        '文章編號': pk,
    })


def 登入(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('首頁')
    return render(request, '文章/登入.html')


def 登出(request):
    logout(request)
    return redirect('首頁')


class 線頂斷詞翻譯(View):

    def get(self, request):
        template = loader.get_template('文章/線頂斷詞翻譯.html')
        context = RequestContext(request, {
            '文章': '',
            '有登入無': request.user.is_authenticated(),
        })
        return HttpResponse(template.render(context))

    def post(self, request):
        確定 = request.POST['確定']
        文章 = request.POST['文章']
        try:
            if 確定 == '斷詞':
                文章 = 斷詞(文章)
            elif 確定 == '翻譯':
                文章 = 翻譯(文章)
        except:
            pass
        template = loader.get_template('文章/線頂斷詞翻譯.html')
        context = RequestContext(request, {
            '文章': 文章,
            '有登入無': request.user.is_authenticated(),
        })
        return HttpResponse(template.render(context))
