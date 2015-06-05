# -*- coding: utf-8 -*-
import urllib.request
import json

class 對語料庫網站掠資料落來:
	# [{'文號':文號,'日期':上尾修改時間,'閩南語':'...','國語':'...'},
	#	 {'文號':文號,'日期':上尾修改時間,'閩南語':'...','國語':'...'},]
	def 掠資料(self):
		# icorpus.iis.sinica.edu.tw/全部題號
		網頁檔案 = urllib.request.urlopen(
			'http://icorpus.iis.sinica.edu.tw/%E5%85%A8%E9%83%A8%E6%96%87%E8%99%9F'
			)
		網頁=網頁檔案.read()
		網頁檔案.close()
		# icorpus.iis.sinica.edu.tw/{0}/揣翻譯對應/
		掠文章 = 'http://icorpus.iis.sinica.edu.tw/{0}/%E6%8F%A3%E7%BF%BB%E8%AD%AF%E5%B0%8D%E6%87%89'
		資料 = []
		for 文章號碼 in json.loads(網頁.decode('UTF-8'))[:]:
			文章內容檔案 = urllib.request.urlopen(掠文章.format(文章號碼))
			文章內容=文章內容檔案.read()
			文章內容檔案.close()
#			 print(文章內容.decode('UTF-8'))
#			 print(掠文章.format(文章號碼))
#			 print(文章號碼)
			翻譯 = json.loads(文章內容.decode('UTF-8'))
			資料.append(翻譯)
		return 資料
		
if __name__ == '__main__':
	掠資料落來 = 對語料庫網站掠資料落來()
	資料 = 掠資料落來.掠資料()
	print(資料[:10])
