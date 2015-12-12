
from django.contrib.auth.models import User
from django.test import TestCase
from 文章.models import 何澤政文章


class 加新文章試驗(TestCase):

    def setUp(self):
        User.objects.create_user(username='噶哈巫族', password='kaxabu')
        self.client.login(username='噶哈巫族', password='kaxabu')

    def test_有加新文章(self):
        文章數 = 何澤政文章.objects.all().count()
        self.加一篇文章()
        self.assertEqual(何澤政文章.objects.all().count(), 文章數 + 1)

    def test_文章加兩擺無效(self):
        self.加一篇文章()
        文章數 = 何澤政文章.objects.all().count()
        self.加一篇文章()
        self.assertEqual(何澤政文章.objects.all().count(), 文章數)

    def 加一篇文章(self):
        self.client.post('/加新文章/', {
            '分類': '社會',
            '原本標題': '埔里四庄番-噶哈巫族',
            '原本內容': '''感謝各位支持噶哈巫語分類辭典,不好意思讓大家久等了~~~~
想必大家已經迫不急待想要拿到這本 <噶哈巫分類辭典> 了
小編在此公告購書事宜及書籍價格~~~~''',
        })
