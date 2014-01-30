import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from article.models import Article
from datetime import date

with open('data/article_frank.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        if line[0]=='(':
            list = line[1:-2].split('\', \'')
            try:
                l = list[0].split('\'')
                l2 = list[8].split('\'')
                l3 = l2[1].split(',')
                l4 = list[11].split('\'')
                Article.objects.create(title=l[1], 
                    title_translation=list[1],
                    date=date(int(list[2]), int(list[3]), int(list[6])),
                    content=list[4],
                    origin_content=list[5],
                    assign_name=list[7],
                    category=l2[0],
                    status_m=l3[1],
                    status_p=l3[2],
                    status_t=l3[3],
                    status_f=l3[4],
                    TaiLuo=l2[2],
                    JiaoLuo=list[9],
                    TongYong=list[10],
                    HaoLuo=l4[0],
                    is_backed_up=int(l4[1][2:-1])
                    )
            except ValueError:
                print(line)
f.closed