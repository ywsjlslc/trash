import requests
import json
import sys
import time

def Get_ruid(Id):
	url = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=" + str(Id)
	ruid = json.loads(requests.get(url).text)["data"]["room_info"]["uid"]
	return ruid

def Print(info , cnt): 
	i = 0
	while 1: 
			try: 
				print(f'{cnt}\tuid:{info[i]["uid"]}') 
				i = i + 1
				cnt = cnt + 1
			except: 
				break

def level(Id): 
	url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(Id) + '&jsonp=jsonp'
	while 1: 
		try: 	
			text = json.loads(requests.get(url).text)["data"]["level"]
			break
		except: 
			print("叔叔py小")
			time.sleep(1)
	return text

def Cnt(info , a): 
	i = 0
	while 1: 
			try: 
				a[level(info[i]["uid"])] += 1
			except: 
				break
			i = i + 1
	return a
	
def main(Id , ruid): 
	a = [0 , 0 , 0 , 0 , 0 , 0 , 0]
	page = 1 
	cnt = 1
	url = "https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid="+ str(Id) +"&page=1&ruid="+ str(ruid) +"&page_size=5"
	text = json.loads(requests.get(url).text)
	Max =  text["data"]["info"]["page"]
	top3 = text["data"]["top3"]
	a = Cnt(top3 , a)
	Print(top3 , cnt)
	cnt += 3
	while 1: 
		url = "https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid="+ str(Id) +"&page="+ str(page) + "&ruid="+ str(ruid) +"&page_size=5" 
		page = page + 1 
		while 1: 
			try: 
				info = json.loads(requests.get(url).text)["data"]["list"]
				break
			except: 
				1
		a = Cnt(info , a)
		Print(info , cnt)
		# print(a)
		cnt += 5
		if page > Max : 
			break
	print(a)

if __name__ == '__main__': 
	Id = sys.argv[1]
	ruid = Get_ruid(Id)
	main(Id , ruid)

