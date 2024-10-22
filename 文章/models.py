from django.db import models
from 文章.斷詞翻譯 import 斷詞
from 文章.斷詞翻譯 import 翻譯
from 文章.文章整理 import 文章整理

文章整理工具 = 文章整理()


class 何澤政文章(models.Model):
    頭一擺翻譯時間 = models.DateField(auto_now_add=True)
    上尾修改時間 = models.DateField(auto_now=True)
    分類 = models.CharField(max_length=100)
    原本標題 = models.CharField(max_length=255)
    原本內容 = models.TextField()
    斷詞標題 = models.CharField(blank=True, max_length=255)
    斷詞內容 = models.TextField(blank=True)
# 	assign_name = models.CharField(max_length=100)
    # 原本欲審核用，已經無效
# 	status_m = models.SmallIntegerField()
# 	status_p = models.SmallIntegerField()
# 	status_t = models.SmallIntegerField()
# 	status_f = models.SmallIntegerField()
    教羅標題 = models.CharField(blank=True, max_length=255)
# 	TaiLuo = models.TextField(blank=True)
    教羅內容 = models.TextField(blank=True)
# 	TongYong = models.TextField(blank=True)
# 	HaoLuo = models.TextField(blank=True)
# 	is_backed_up = models.BooleanField()

    def __str__(self):
        return self.原本標題

    @classmethod
    def 這標題有用過無(cls, 原本標題):
        return cls.objects.filter(原本標題=原本標題).exists()

    def save(self, *args, **kwargs):
        self.斷詞標題 = 文章整理工具.轉文章空白(self.斷詞標題)
        self.斷詞內容 = 文章整理工具.轉文章空白(self.斷詞內容)
        self.教羅標題 = 文章整理工具.轉文章空白(self.教羅標題)
        self.教羅內容 = 文章整理工具.轉文章空白(self.教羅內容)
        super(何澤政文章, self).save(*args, **kwargs)

    def 自動斷詞(self):
        if self.斷詞標題 == '':
            try:
                self.斷詞標題 = 斷詞(self.原本標題)
                self.save()
            except:
                pass
        if self.斷詞內容 == '':
            try:
                self.斷詞內容 = 斷詞(self.原本內容)
                self.save()
            except:
                pass

    def 自動翻譯(self):
        if self.教羅標題 == '':
            try:
                self.教羅標題 = 翻譯(self.斷詞標題)
                self.save()
            except:
                pass
        if self.教羅內容 == '':
            try:
                self.教羅內容 = 翻譯(self.斷詞內容)
                self.save()
            except:
                pass
