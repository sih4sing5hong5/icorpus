# 臺華新聞語料庫

中研院資訊所陳孟彰老師支持的計劃，[網站在此](http://icorpus.iis.sinica.edu.tw/)。


## 安裝
```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install django
```

走django
```bash
PYTHONPATH=../tai5_uan5_gi5_gi2_kang1_ku7/ python manage.py runserver
```

訓練翻譯模型
```bash
PYTHONPATH=../tai5_uan5_gian5_gi2_kang1_ku7/ python 文章/模型訓練/臺華新聞做語料.py
PYTHONPATH=../tai5_uan5_gian5_gi2_kang1_ku7/ python 文章/模型訓練/摩西模型訓練.py
```

走翻譯服務
```bash
PYTHONPATH=../tai5_uan5_gian5_gi2_kang1_ku7/ python 文章/摩西服務.py 
```