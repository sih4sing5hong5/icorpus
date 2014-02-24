import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from article.models import Article
from datetime import date
from dateutil.relativedelta import relativedelta

class insert_article:
	def tok8_tsu1_liau7(self):
		tsu1_liau7=[]
		with open('db/data/article_frank.txt', 'r', encoding="UTF-8") as f:
			for line in f:
				if line[0]=='(':
					list = line[1:-2].split('\', \'')
					try:
						l = list[0].split('\'')
						l2 = list[8].split('\'')
						l3 = l2[1].split(',')
						l4 = list[11].split('\'')
						
						id=int(list[0].split(',')[0])
						datea=date(int(list[2]), int(list[3]), int(list[6]))
						category=l2[0]
						origin_title=l[1].replace(' ','')
						origin_content=list[5]
						title=l[1]
						content=list[4]
						title_translation=list[1]
		#					assign_name=list[7],
		#					status_m=l3[1],
		#					status_p=l3[2],
		#					status_t=l3[3],
		#					status_f=l3[4],
						TaiLuo=l2[2]
						JiaoLuo=list[9]
		#					TongYong=list[10],
						HaoLuo=l4[0]
		#				print(JiaoLuo)
		#				print(list)
						si7_JiaoLuo=True
						if JiaoLuo.strip()=='':
							if TaiLuo.strip()=='' and HaoLuo.strip()=='':
								print('bo5')
							elif TaiLuo.strip()=='' and HaoLuo.strip()!='':
								si7_JiaoLuo=False
								JiaoLuo=HaoLuo.strip()
							elif TaiLuo.strip()!='' and HaoLuo.strip()=='':
								JiaoLuo=TaiLuo
							elif TaiLuo.strip()!='' and HaoLuo.strip()!='':
								print('bo5 4')
					except ValueError:
						print(line)
					else:
						tsu1_liau7.append((si7_JiaoLuo,id,datea,category,
								origin_title.strip(),origin_content.strip(),
								title.strip(),content.strip(),
								title_translation.strip(),JiaoLuo.strip()))
		return tsu1_liau7
	def tsu2_li2(self):
		tsu1_liau7=sorted(self.tok8_tsu1_liau7(),key=lambda tsu1:tsu1[1])
		cnt=1
		now=date(2008,11,6)
		for a in tsu1_liau7[:]:
			if a[0] and a[2]<date(2009,1,1):
				print(a[2])
				
			print(now)
			cnt+=1
			if cnt==2:
				cnt=0
				now=now+relativedelta(days=1)
				while now.weekday()>=5:
					now=now+relativedelta(days=1)
		for a in tsu1_liau7:
		    if a[4]=='鬼辣椒辣度破百萬男子嗆到送醫':
			      print(a[2])
		  #2008-11-6 7 7
		  #鬼辣椒 辣度 破百萬 男子 嗆到 送醫 2009-3-15
		#			  Article.objects.create(
icorpus_article=insert_article()
icorpus_article.tsu2_li2()
sdfap