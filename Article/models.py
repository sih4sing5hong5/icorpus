from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    title_translation = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()
    origin_content = models.TextField()
    assign_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status_m = models.SmallIntegerField()
    status_p = models.SmallIntegerField()
    status_t = models.SmallIntegerField()
    status_f = models.SmallIntegerField()
    TaiLuo = models.TextField()
    JiaoLuo = models.TextField()
    TongYong = models.TextField()
    HaoLuo = models.TextField()
    is_backed_up = models.BooleanField()
    
    