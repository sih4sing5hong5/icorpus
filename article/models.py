from django.db import models

class Article(models.Model):
	date = models.DateField()
	category = models.CharField(max_length=100)
	origin_title = models.CharField(max_length=255)
	origin_content = models.TextField()
	title = models.CharField(blank=True,max_length=255)
	content = models.TextField(blank=True)
#	assign_name = models.CharField(max_length=100)
	#原本欲審核用，已經無效
#	status_m = models.SmallIntegerField()
#	status_p = models.SmallIntegerField()
#	status_t = models.SmallIntegerField()
#	status_f = models.SmallIntegerField()
	title_translation = models.CharField(blank=True,max_length=255)
	TaiLuo = models.TextField(blank=True)
	JiaoLuo = models.TextField(blank=True)
#	TongYong = models.TextField(blank=True)
	HaoLuo = models.TextField(blank=True)
#	is_backed_up = models.BooleanField()
	
	def __str__(self):
		return self.title
	
	