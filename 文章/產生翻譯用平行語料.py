
from 文章.models import 何澤政文章
'''
使用方法
python3 manage.py shell
from 文章.產生翻譯用平行語料 import 產生翻譯用平行語料
產生翻譯用平行語料()
'''
class 產生翻譯用平行語料():
    def __init__(self):
    	for 文章 in 何澤政文章.objects.order_by('pk'):
    		國語 = 文章.斷詞標題 + '\n' + 文章.斷詞內容
    		教羅 = 文章.教羅標題 + '\n' + 文章.教羅內容
    		國語 = 國語.strip()
    		教羅 = 教羅.strip()
    		文章國語 = 國語.split('\n')
    		文章音標 = 教羅.split('\n')
    		if len(文章國語) != len(文章音標):
    			print('國語佮音標對無齊：{0}'.format(文章.pk))
    			continue
#     		print(國語,)
#     		print(教羅,)

if __name__=='__main__':
	產生翻譯用平行語料()