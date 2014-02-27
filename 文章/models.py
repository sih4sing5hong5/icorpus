from django.db import models
from 文章.斷詞翻譯 import 斷詞

class 何澤政文章(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	分類 = models.CharField(max_length=100)
	原本標題 = models.CharField(max_length=255)
	原本內容 = models.TextField()
	斷詞標題 = models.CharField(blank=True,max_length=255)
	斷詞內容 = models.TextField(blank=True)
#	assign_name = models.CharField(max_length=100)
	#原本欲審核用，已經無效
#	status_m = models.SmallIntegerField()
#	status_p = models.SmallIntegerField()
#	status_t = models.SmallIntegerField()
#	status_f = models.SmallIntegerField()
	教羅標題 = models.CharField(blank=True,max_length=255)
# 	TaiLuo = models.TextField(blank=True)
	教羅內容 = models.TextField(blank=True)
#	TongYong = models.TextField(blank=True)
# 	HaoLuo = models.TextField(blank=True)
#	is_backed_up = models.BooleanField()
	
	def __str__(self):
		return self.原本標題
	def 自動斷詞(self):
		if self.斷詞標題=='':
			try:
				self.斷詞標題=斷詞(self.原本標題)
				self.save()
			except:
				pass
		if self.斷詞內容=='':
			try:
				self.斷詞內容=斷詞(self.原本內容)
				self.save()
			except:
				pass