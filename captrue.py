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
	return cnt
def level(Id , cnt): 
	url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(Id) + '&jsonp=jsonp'
	while 1: 
		try: 	
			info = json.loads(requests.get(url).text)
			text = info["data"]["level"]
			print(f'{cnt}\tlv.{text}\tuid:{Id:<15}name: {info["data"]["name"]}')
			break
		except: 
			# print("叔叔py小")
			time.sleep(1)
	return [text , cnt + 1]

def Cnt(info , a , cnt): 
	i = 0
	while 1: 
			try: 
				[lv , cnt] = level(info[i]["uid"] , cnt)
				a[lv] += 1
			except: 
				break
			i = i + 1
	return [a , cnt]
	
def main(Id , ruid): 
	a = [0 , 0 , 0 , 0 , 0 , 0 , 0]
	page = 1 
	cnt = 1
	url = "https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid="+ str(Id) +"&page=1&ruid="+ str(ruid) +"&page_size=30"
	text = json.loads(requests.get(url).text)
	Max =  text["data"]["info"]["page"]
	top3 = text["data"]["top3"]
	[a , cnt] = Cnt(top3 , a , cnt)
	# cnt = Print(top3 , cnt)
	while 1: 
		url = "https://api.live.bilibili.com/xlive/app-room/v2/guardTab/topList?roomid="+ str(Id) +"&page="+ str(page) + "&ruid="+ str(ruid) +"&page_size=30" 
		page = page + 1 
		while 1: 
			try: 
				info = json.loads(requests.get(url).text)["data"]["list"]
				break
			except: 
				1
		[a , cnt] = Cnt(info , a , cnt)
		# Print(info , cnt)
		# print(a)
		if page > Max : 
			break
	print(a)

if __name__ == '__main__': 
	Id = sys.argv[1]
	ruid = Get_ruid(Id)
	main(Id , ruid)

