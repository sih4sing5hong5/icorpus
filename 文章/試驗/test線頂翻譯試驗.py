# -*- coding: utf-8 -*-
from django.test import TestCase

class 線頂翻譯試驗(TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_一句換逝莫改變(self):
		self.看翻譯結果('現在 正 值 一 期 稻作 的 插秧 季節 ，\n也 是 代 工 耕 作 業 者 最 忙 的 時 候 。', 2)
	def test_無標點的一句換逝莫改變(self):
		self.看翻譯結果('現在 正 值 一 期 稻作 的 插秧 季節 \n也 是 代 工 耕 作 業 者 最 忙 的 時 候 。', 2)
	def test_空一句莫改變(self):
		self.看翻譯結果('現在 正 值 一 期 稻作 的 插秧 季節 ，\n\n也 是 代 工 耕 作 業 者 最 忙 的 時 候 。', 3)
	def 看翻譯結果(self, 文章, 句數):
		回應 = self.client.post('/線頂斷詞翻譯', {
				'確定':'翻譯',
				'文章':文章
		})
		翻了文章 = 回應.context['文章'].strip()
		self.assertEqual(len(翻了文章.split('\n')), 句數, 翻了文章)
