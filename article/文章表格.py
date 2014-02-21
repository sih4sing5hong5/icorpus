from django.forms import ModelForm
from django.forms import Textarea
from django.forms import Select
from article.models import Article

class 文章全部表格(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

分類=[("政治","政治"),
	("社會","社會"),
	("地方","地方"),
	("國際","國際"),
	("財經","財經"),
	("運動","運動"),
	("健康","健康"),
	("教育","教育"),
	("藝文","藝文"),
	("影劇","影劇"),
	("旅遊","旅遊"),
	("生活","生活"),
	("科技","科技"),
	("環境","環境")]
                                                            
class 加新文章表格(ModelForm):
	class Meta:
		model = Article
		fields = ['category', 'origin_title', 'origin_content', ]
		labels = {
			'category':'分類',
            'origin_title': '原始標題',
            'origin_content': '原始內容',
        }
		help_texts = {
            'origin_title': '免斷詞',
            'origin_content': '免斷詞',
        }
		error_messages = {
            'origin_title': {
                'max_length': ("This writer's name is too long."),
            },
        }
		widgets = {
			'category': Select(choices=分類),
		}
		
class 改國語斷詞表格(ModelForm):
	class Meta:
		model = Article
		fields = ['origin_title', 'title', 'origin_content', 'content']
		widgets = {
			'origin_content': Textarea(attrs={'class':'文章','wrap': 'off'}),
			'content': Textarea(attrs={'class':'文章','wrap': 'off'}),
		}


class 改閩南語翻譯表格(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'title_translation', 'content', 'JiaoLuo']
		widgets = {
			'content': Textarea(attrs={'class':'文章','wrap': 'off'}),
			'JiaoLuo': Textarea(attrs={'class':'文章','wrap': 'off'}),
		}
