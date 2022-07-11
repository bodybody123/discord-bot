from ast import JoinedStr
from http.client import responses
import json
import requests
# from hentai import Hentai, Format

# # make a request to nhentai.net
# doujin = Hentai(177013)

# # True
# Hentai.exists(doujin.id)

# # METAMORPHOSIS
# print(doujin.title(Format.Pretty))

# # [Tag(id=3981, type='artist', name='shindol', url='https://nhentai.net/artist/shindol/', count=279)]
# print(doujin.artist[0].name)

# # # ['dark skin', 'group', ... ]
# print([tag.name for tag in doujin.tag])

# # # 2016-10-18 12:28:49+00:00
# # print(doujin.upload_date)

# # # ['https://i.nhentai.net/galleries/987560/1.jpg', ... ]
# print(doujin.image_urls[0])

# # # store all image urls to disk
# # doujin.download(progressbar=True)

response = requests.get("https://yande.re/post.json?tags=loli&limit=5")

def convertJson(jsonData):
  for text in jsonData:
    print(text['jpeg_url'])

convertJson(response.json())
