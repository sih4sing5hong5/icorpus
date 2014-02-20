from django.forms import ModelForm
from article.models import Article

class 文章全部表格(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class 改國語斷詞表格(ModelForm):
	class Meta:
		model = Article
		fields = ['category', 'title', 'content']

class 改閩南語翻譯表格(ModelForm):
	class Meta:
		model = Article
		fields = ['category', 'title']
