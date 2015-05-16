from django.db import models
from django.forms.models import ModelForm

class 華語新聞(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	原本標題 = models.CharField(max_length=255)
	原本內容 = models.TextField()
	斷詞標題 = models.CharField(blank=True, max_length=255)
	斷詞內容 = models.TextField(blank=True)
	狀態 = models.CharField(max_length=20,choices=[('猶未使用', '猶未使用'),
		 ('使用', '使用'),
		 ('傷長', '傷長'),
		 ('語句無順', '語句無順'), ],
		default='猶未使用')

class 華語新聞表格(ModelForm):
	class Meta:
		model = 華語新聞
		fields = '__all__'