from django.forms import ModelForm
from django.forms import Textarea
from django.forms import Select
from 文章.models import 何澤政文章

class 文章全部表格(ModelForm):
	class Meta:
		model = 何澤政文章
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
		model = 何澤政文章
		fields = ['分類', '原本標題', '原本內容', ]
		labels = {
			'分類':'分類',
            '原本標題': '原始標題',
            '原本內容': '原始內容',
        }
		help_texts = {
            '原本標題': '免斷詞',
            '原本內容': '免斷詞',
        }
		error_messages = {
            '原本標題': {
                'max_length': ("This writer's name is too long."),
            },
        }
		widgets = {
			'分類': Select(choices=分類),
		}
		
class 改國語斷詞表格(ModelForm):
	class Meta:
		model = 何澤政文章
		fields = ['原本標題', '斷詞標題', '原本內容', '斷詞內容']
		widgets = {
			'原本內容': Textarea(attrs={'class':'文章','wrap': 'off'}),
			'斷詞內容': Textarea(attrs={'class':'文章','wrap': 'off'}),
		}


class 改閩南語翻譯表格(ModelForm):
	class Meta:
		model = 何澤政文章
		fields = ['斷詞標題', '教羅標題', '斷詞內容', '教羅內容']
		widgets = {
			'斷詞內容': Textarea(attrs={'class':'文章','wrap': 'off'}),
			'教羅內容': Textarea(attrs={'class':'文章','wrap': 'off'}),
		}
