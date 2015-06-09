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

走翻譯服務
```bash
PYTHONPATH=../tai5_uan5_gian5_gi2_kang1_ku7/ python 文章/摩西服務.py 
```