import json
import pandas as pd

json_data = '''
{
  "code": 200,
  "message": "success",
  "data": {
    "comics": [
      {
        "_id": "62bfe3f32f2e9338c6593d1d",
        "title": "きて。 愛我。",
        "author": "ヘリを",
        "totalViews": 490261,
        "totalLikes": 10784,
        "pagesCount": 221,
        "epsCount": 1,
        "finished": true,
        "categories": [
          "長篇",
          "純愛",
          "單行本",
          "姐姐系",
          "妹妹系"
        ],
        "thumb": {
          "originalName": "風的工房003.jpg",
          "path": "tobeimg/czcL7qSSH92eoiGzhxzQXf0tK41iMnVvbezInqdzpe4/rs:fill:300:400:0/g:sm/aHR0cHM6Ly9zdG9yYWdlLWIucGljYWNvbWljLmNvbS9zdGF0aWMvOWZjNGI3MGEtNDQ2ZC00NmY1LWJmMjgtNzliN2QwM2EyNzMzLmpwZw.jpg",
          "fileServer": "https://storage-b.picacomic.com"
        },
        "viewsCount": 490261,
        "leaderboardCount": 306596
      },
      {
        "_id": "62bccc5be2f5440c99db4244",
        "title": "[3D漫画]母亲的奇异系统1-5",
        "author": "听话的阿伟",
        "totalViews": 1288384,
        "totalLikes": 6823,
        "pagesCount": 557,
        "epsCount": 5,
        "finished": true,
        "categories": [
          "全彩",
          "長篇",
          "CG雜圖"
        ],
        "thumb": {
          "originalName": "006.jpg",
          "path": "tobeimg/B-mfAMtueKTrlX0WY0z6q2vm05aoCCQVqAQWCQxwOK0/rs:fill:300:400:0/g:sm/aHR0cHM6Ly9zdG9yYWdlLWIucGljYWNvbWljLmNvbS9zdGF0aWMvODU0ODkwNmItNDZkNS00MWY0LTk2YjMtZTY4NmI0ZmI0Mzc2LmpwZw.jpg",
          "fileServer": "https://storage-b.picacomic.com"
        },
        "viewsCount": 1288384,
        "leaderboardCount": 215309
      },
      {
        "_id": "61e43fa6b93f6b06e931a80d",
        "title": " 全部君のせいだ。III [中国翻訳] [DL版]",
        "author": "毛玉牛乳 (玉之けだま)",
        "totalViews": 1834253,
        "totalLikes": 26089,
        "pagesCount": 96,
        "epsCount": 1,
        "finished": true,
        "categories": [
          "長篇",
          "妹妹系",
          "非人類"
        ],
        "thumb": {
          "originalName": "01__001.jpg",
          "path": "tobeimg/jCDIyVo-SDtK7z0zKB4L7WnUGQFg4Y8UB6doyEK6jQY/rs:fill:300:400:0/g:sm/aHR0cHM6Ly9zdG9yYWdlMS5waWNhY29taWMuY29tL3N0YXRpYy84NzU4NTM0MS00ZjQ0LTRlYzctYTNjNS1jNzEyYzZmZWU5NjguanBn.jpg",
          "fileServer": "https://storage1.picacomic.com"
        },
        "viewsCount": 1834253,
        "leaderboardCount": 205800
      }
    ]
  }
}
'''

# 解析JSON数据
data = json.loads(json_data)

# 提取需要的字段
comics = data['data']['comics']
filtered_comics = []

for comic in comics:
    filtered_comics.append({
        '_id': comic['_id'],
        'title': comic['title'],
        'author': comic['author'],
        'categories': ', '.join(comic['categories'])
    })

# 创建DataFrame
df = pd.DataFrame(filtered_comics)

# 导出到Excel
df.to_excel('comics.xlsx', index=False)
