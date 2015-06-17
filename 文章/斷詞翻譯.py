
from 文章.文章整理 import 文章整理
from 臺灣言語工具.斷詞.中研院.斷詞用戶端 import 斷詞用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡


__文章整理 = 文章整理()
_分析器 = 拆文分析器()
_譀鏡 = 物件譀鏡()
_摩西用戶 = 摩西用戶端(埠=8500, 編碼器=語句編碼器())
	
def 斷詞(語句):	
	斷詞用戶 = 斷詞用戶端()
	整理後語句 = __文章整理.轉文章空白(語句)
	全部斷詞結果=[]
	for 華語句 in 整理後語句.split('\n'):
		章物件=_分析器.轉做章物件(華語句)
		華語斷詞章物件=斷詞用戶.斷詞(章物件)
		華語斷詞語句=_譀鏡.看型(華語斷詞章物件, 物件分詞符號=' ', 物件分句符號='\n')
		全部斷詞結果.append(華語斷詞語句)
	return '\n'.join(全部斷詞結果)

def 翻譯(語句):
	整理後語句 = __文章整理.轉文章空白(語句)
	華語章物件 = _分析器.轉做章物件(整理後語句)
	閩南語章物件, _翻譯結構華語章物件, _分數 = _摩西用戶.翻譯(華語章物件)
	return _譀鏡.看型(閩南語章物件,
		 物件分詞符號=' ', 物件分字符號='-', 物件分句符號='').replace('N', 'nn')
