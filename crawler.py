import requests, json, sys
from bs4 import BeautifulSoup
def getURL(s):
    return "http://neoj.sprout.tw/api/user/"+s+"/statistic"
def main():
  a=sys.argv[1]
  b=sys.argv[2]
  data = {"text": "{}"}
  req = requests.post(getURL(a),json=data)
  user1=json.loads(req.text)
  user1AC=[]
  req = requests.post(getURL(b),json=data)
  user2=json.loads(req.text)
  user2AC=[]

  for k in user1["tried_problems"]:
      if user1["tried_problems"][k]["result"]==1:
          user1AC.append(int(k))
  user1AC.sort()
  for k in user2["tried_problems"]:
      if user2["tried_problems"][k]["result"]==1:
          user2AC.append(int(k))
  user2AC.sort()

  both=[]
  for k in user1AC:
      if k in user2AC:
          both.append(k)
  only1=[]
  for k in user1AC:
      if not k in user2AC:
          only1.append(k)
  only2=[]
  for k in user2AC:
      if not k in user1AC:
          only2.append(k)
  opt = {"both":both, "only1":only1, "only2":only2}
  print(json.dumps(opt))
if len(sys.argv)>2:
  main()
