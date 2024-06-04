import operator
import os
import random
import zipfile
import pandas as pd
from configparser import ConfigParser
from datetime import datetime


def convert_file_name(name: str) -> str:
    # windows的文件夹不能带特殊字符,需要处理下文件夹名
    for i, j in ("/／", "\\＼", "?？", "|︱", "\"＂", "*＊", "<＜", ">＞", ":-"):
        name = name.replace(i, j)
    name = name.replace(" ", "")
    return name


def get_cfg(section: str, key: str):
    parser = ConfigParser()
    parser.read('./config.ini', encoding='utf-8')
    return dict(parser.items(section))[key]

def export_leadborad(comics):
    filtered_comics = []

    for comic in comics:
        filtered_comics.append({
            '_id': comic['_id'],
            'title': comic['title'],
            'author': comic['author'],
            'categories': ', '.join(comic['categories'])
        })

    df = pd.DataFrame(filtered_comics)
    df.to_excel('comics.xlsx', index=False)

def export_comic_list(comics):
    filtered_comics = []

    for comic in comics:
        filtered_comics.append({
            '_id': comic['_id'],
            'title': comic['title'],
            'author': comic['author'],
            'categories': ', '.join(comic['categories'])
        })

    df = pd.DataFrame(filtered_comics)
    df.to_excel('comics.xlsx', index=False)



# 获取待下载的章节
def filter_comics(comic, episodes) -> list:
    ids = open('./downloaded.txt', 'r').read().split('\n')
    # 已下载过的漫画,执行增量更新
    if comic["_id"] in ids:
        episodes = [i for i in episodes if
                    (datetime.strptime(i['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ') - get_latest_run_time()).total_seconds() > 0]
    # 过滤掉指定分区的本子
    categories_rule = os.environ["CATEGORIES_RULE"]
    categories = os.environ["CATEGORIES"].split(',')
    # 漫画的分区和用户自定义分区的交集
    intersection = set(comic['categories']).intersection(set(categories))
    if categories:
        # INCLUDE: 包含任意一个分区就下载  EXCLUDE: 包含任意一个分区就不下载
        if (categories_rule == 'EXCLUDE' and len(intersection) == 0) or (
                categories_rule == 'INCLUDE' and len(intersection) > 0):
            return episodes
        else:
            return []
    return episodes

def download(self, name: str, i: int, url: str):
    path = './comics/' + convert_file_name(name) + '/' + str(i + 1).zfill(4) + '.jpg'
    if os.path.exists(path):
        return

    f = open(path, 'wb')
    f.write(self.http_do("GET", url=url).content)
    f.close()