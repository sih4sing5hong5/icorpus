from django.forms import ModelForm
from django.forms import Textarea
from article.models import Article

class 文章全部表格(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

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
