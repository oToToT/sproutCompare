#!/usr/bin/python3 -O
import requests, json, sys
from bs4 import BeautifulSoup
def getURL(s):
    return "http://neoj.sprout.tw/api/user/"+s+"/statistic"
def main():
  a,b=sys.argv[1:3]
  data = {"text": "{}"}
  req = requests.post(getURL(a),json=data)
  user1=json.loads(req.text)
  user1AC=sorted([ int(k) for k in user1["tried_problems"] if user1["tried_problems"][k]["result"]==1 ])
  req = requests.post(getURL(b),json=data)
  user2=json.loads(req.text)
  user2AC=sorted([ int(k) for k in user2["tried_problems"] if user2["tried_problems"][k]["result"]==1 ])

  both=[k for k in user1AC if k in user2AC]
  only1=[k for k in user1AC if not k in user2AC]
  only2=[k for k in user2AC if not k in user1AC]

  opt = {"both":both, "only1":only1, "only2":only2}
  print(json.dumps(opt))
if len(sys.argv)>2:
  main()
