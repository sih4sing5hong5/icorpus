# 臺華新聞語料庫

中研院資訊所陳孟彰老師的計劃，檔案是`icorpus.json`。自2008-11-06開始到2016-02-15結束，收集3266篇新聞，攏總83544句。算標點符號，台語504037詞、1030671字，華語501202詞、1028218字。

計劃後，閣有人修改，佇`icorpus.yaml`。

## Frank何澤政的處理方法
1. 先揣適當的新聞
2. 鉸做合理的長度
3. 修正錯字
4. 接著查辭典
5. 把文章放到資料庫
6. 接著檢查斷詞部分
7. 接著檢查翻譯的部分
8. 然後還要整篇再看一次

開的時間，前後加起來不只四小時

## 語料授權
![創用 CC 授權條款](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

本著作[係採用創用 CC 姓名標示-非商業性-相同方式分享 4.0 國際 (CC BY-NC-SA 4.0) 授權條款](http://creativecommons.org/licenses/by-nc-sa/4.0/)授權。

授權人：中央研究院 資訊科學研究所 陳孟彰研究員

### 語料
會當到[網站](http://icorpus.iis.sinica.edu.tw/)看翻譯的結果，嘛會當掠規个網站的[json](https://github.com/sih4sing5hong5/icorpus/blob/master/icorpus.json)。

## 程式授權
程式部份用[MIT授權](https://github.com/sih4sing5hong5/icorpus/blob/master/LICENSE)。


### 安裝
```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

走django
```bash
python manage.py runserver
```

訓練翻譯模型
```bash
python 文章/模型訓練/臺華新聞做語料.py
python 文章/模型訓練/摩西模型訓練.py
```

走翻譯服務
```bash
python 文章/摩西服務.py 
```
