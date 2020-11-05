import json
# import random
from evaluate.models import Songs

Songs.objects.all().delete()
with open('data.json') as json_file:
	dat = json.load(json_file)

garbage = ["(Bestwap)","(bestwap)","(bestwap.in)","(Bestwap.in)","Normal","Low","High","Quality","64","128","320","Kbps","Bestwap.in","2020","2013","2014","2015","2016","2017","2018","2019", "Mp3", "Songs","songs","Title","(Punjabi)(bestwap.in)","Bestwap","(Title","Track)","Track","Song","song"]
def remspace(st):
	temp = st.split(' ')
	st=""
	for i in temp:
		st = st+i
		st = st+"%20"
	st = st[:-3]
	return st

# print(remspace("an df er"))

def remunder(st):
	
	ls=[]
	temp = st.split('_')
	for i in temp:
		ls.extend(i.split(' '))
	# print(ls)
	ans = ""
	for i in ls:
		if i not in garbage:
			if "(bestwap.in)" in i or "(Bestwap.in)" in i:
				i = i[:-12]
			ans = ans+i
			ans = ans+" "
	if(len(ans)==0):
		return "Unknown"
	else:
		return ans


# print(remunder("an_ur_aj"))

i=0
mp={"as":0,}
# random.shuffle(dat,random)
for item in dat:
	i=i+1
	itemlink = item.split('++')[0]
	itemartist = item.split('++')[1]
	if itemartist.split(' ')[0]=="Download" or itemartist=='\n' or len(itemartist)>50:
		itemartist="Unknown"
	itemtitle = itemlink.split('/')[-1]
	itemtitle = itemtitle[:-4]
	if len(itemtitle)>50:
		itemtitle=itemtitle[:42]+'...'
	itemalbum = itemlink.split('/')[-2]
	if(itemalbum[0]=='6'):
		itemalbum = itemlink.split('/')[-3]
	if len(itemalbum)>50:
		itemalbum=itemalbum[:42]+'...'
	itemalbum = remunder(itemalbum)
	itemlink = remspace(itemlink)
	itemartist = remunder(itemartist)
	itemtitle = remunder(itemtitle)
	key = itemtitle+itemalbum+itemartist
	if(mp.get(key)):
		continue
	else:
		mp[key]=1
		# if(i>2000 and i<2300):
			# print(itemtitle," --- ",itemalbum,"---", itemartist)
		# print(itemlink)
		if len(itemlink)<200:
			tempsong = Songs(songTitle = itemtitle, songAlbum = itemalbum, songSinger= itemartist, link= itemlink)
			tempsong.save()

 