import requests
from time import sleep
from random import randint

token=''

videos=requests.get('https://api.vk.com/method/video.get', params={'access_token':token, 'v':'5.103', 'count': '200'}).json()
videos=videos['response']['items']
print(len(videos))
proc=(int(len(videos))) / 100
time=1
u=(int(len(videos))) / 100
for video in videos:
	delete_video=requests.get('https://api.vk.com/method/video.delete',params={'access_token': token, 'v':'5.103', 'target_id': '186752691', 'owner_id': video['owner_id'], 'video_id': video['id']}).json()
	print(str(delete_video) + ' ' + str(u) + '%' + ' ' + str(time))
	u+=proc
	time+=1
	sleep(randint(0,2))
