
class 文章整理:
	def 轉文章空白(self, 文章):
		return '\n'.join(self.轉語句陣列空白(文章.split('\n'))).strip()
	def 轉語句陣列空白(self, 語句陣列):
		正常空白的文章 = []
		for 一逝 in 語句陣列:
			正常空白的文章.append(self.轉語句空白(一逝))
		return 正常空白的文章
	def 轉語句空白(self, 一逝):
		處理掉空白無仝佮重複 = ' '.join(一逝.split()).strip()
		連字符加的空白 = 處理掉空白無仝佮重複.replace('- ', ' ').replace(' -', '-')
		return 連字符加的空白
