import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from 文章.models import 何澤政文章
from datetime import date
from dateutil.relativedelta import relativedelta
from db.lcs import lcs_len

class insert_文章:
	def tok8_tsu1_liau7(self):
		tsu1_liau7 = []
		with open('db/data/article_frank.txt', 'r', encoding = "UTF-8") as f:
			for line in f:
				if line[0] == '(':
					list = line[1:-2].split('\', \'')
					try:
						l = list[0].split('\'')
						l2 = list[8].split('\'')
						l3 = l2[1].split(',')
						l4 = list[11].split('\'')

						id = int(list[0].split(',')[0])
						datea = date(int(list[2]), int(list[3]), int(list[6]))
						分類 = l2[0]
						原本標題 = l[1].replace(' ', '')
						原本內容 = list[5]
						斷詞標題 = l[1]
						斷詞內容 = list[4]
						教羅標題 = list[1]
		# 					assign_name=list[7],
		# 					status_m=l3[1],
		# 					status_p=l3[2],
		# 					status_t=l3[3],
		# 					status_f=l3[4],
						TaiLuo = l2[2]
						教羅內容 = list[9]
		# 					TongYong=list[10],
						HaoLuo = l4[0]
						si7_教羅內容 = True
						if 教羅內容.strip() == '':
							if TaiLuo.strip() == '' and HaoLuo.strip() == '':
								print('bo5')
							elif TaiLuo.strip() == '' and HaoLuo.strip() != '':
								si7_教羅內容 = False
								教羅內容 = HaoLuo.strip()
							elif TaiLuo.strip() != '' and HaoLuo.strip() == '':
								教羅內容 = TaiLuo
							elif TaiLuo.strip() != '' and HaoLuo.strip() != '':
								print('bo5 4')
					except ValueError:
						print(line)
					else:
						tsu1_liau7.append((si7_教羅內容, id, datea, 分類,
								原本標題.strip(), 原本內容.strip(),
								斷詞標題.strip(), 斷詞內容.strip(),
								教羅標題.strip(), 教羅內容.strip()))
		return tsu1_liau7
	def tsu2_li2(self):
		tsu1_liau7 = sorted(self.tok8_tsu1_liau7(), key = lambda tsu1:tsu1[1])
		cnt = 1
		一開始= date(2008, 11, 6)
		推算的時間 =一開始
		日期=self.看日期()
# 		print(日期[:5])
		for 資料 in tsu1_liau7[:]:
			if 資料[0]:
	# 			print(now)
				查檔名的時間=self.揣時間(日期, 資料[4])
	# 			print(資料[4],查檔名的時間,資料[2],推算的時間)
				if 查檔名的時間!=None:
					if 查檔名的時間>一開始:
# 						if 推算的時間>查檔名的時間+relativedelta(months=-6):# or 推算的時間>查檔名的時間-relativedelta(months=-12):
						推算的時間=查檔名的時間
# 				else:
# 					print(資料[4],'查無時間','編輯時間',資料[2],'推算的時間',推算的時間)
				if 資料[4]<推算的時間:
					推算的時間=資料[4]
				print('編輯',資料[2],'推算',推算的時間,'查檔名',查檔名的時間,資料[4],)
				if 資料[4] == '鬼辣椒辣度破百萬男子嗆到送醫':
					推算的時間 = date(2009, 3, 15)
					
				何澤政文章.objects.create(
					頭一擺翻譯時間=推算的時間,
					上尾修改時間=資料[2],
					分類=資料[3],
					原本標題=資料[4],
					原本內容=資料[5],
					斷詞標題=資料[6],
					斷詞內容=資料[7],
					教羅標題=資料[8],
					教羅內容=資料[9],)
				cnt += 1
				if cnt == 2:
					cnt = 0
					推算的時間 = 推算的時間 + relativedelta(days = 1)
					while 推算的時間.weekday() >= 5:
						推算的時間 = 推算的時間 + relativedelta(days = 1)
		  # 2008-11-6 7 7
		  # 鬼辣椒 辣度 破百萬 男子 嗆到 送醫 2009-3-15
	def 揣時間(self,日期,標題):
		上長=0
		揀著=None
		上少=len(標題)/2
		for 日, 標 in 日期:
			長度=lcs_len(標, 標題)[0][-1][-1]
			if 長度>上少 and 長度>上長:
				揀著=日
				上長=長度
		return 揀著
	def 看日期(self):
		資料=[]
		for 檔名 in open('db/data/檔名'):
			檔名 = 檔名.split('.')[0]
			日期, 標題 = 檔名[:8].strip(), 檔名[8:].strip()
# 			print(日期[:4],日期[4:8],標題)
			資料.append((date(int(日期[:4]),int(日期[4:6]),int(日期[6:8])), 標題))
		return 資料

icorpus_文章 = insert_文章()
icorpus_文章.tsu2_li2()
sdfap
