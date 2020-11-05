import json
import random
from evaluate.models import Songs

Songs.objects.all().delete()
with open('data.json') as json_file:
	dat = json.load(json_file)
numbers=["01","02","03","04","05","06","07","08","09"]
garbage = ["(",")","BestWap.in","bestwap.in","Bestwap.in","BestWap.In","Bestwap.In","( Bestwap )","(Bestwap)","(bestwap)","( bestwap )","(bestwap.in)","( bestwap.in )","(bestwap.In)","( bestwap.In )","(Bestwap.in)","( Bestwap.in )","(Bestwap.In)","( Bestwap.In )","( BestWap )","(BestWap)","(bestWap)","( bestWap )","(bestWap.in)","( bestWap.in )","(bestWap.In)","( bestWap.In )","(BestWap.in)","( BestWap.in )","(BestWap.In)","( BestWap.In )","Normal","Low","High","Quality","64","128","320","Kbps","Bestwap.in","2020","2013","2014","2015","2016","2017","2018","2019", "Mp3", "Songs","songs","Title","(Punjabi)(bestwap.in)","Bestwap","(Title","Track)","Track","Song","song","-","()"]
garbage.extend(numbers)
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
	
	# ls=[]
	# temp = st.split('_')
	# for i in temp:
	# 	ls.extend(i.split(' '))
	# # print(ls)
	# ans = ""
	# for i in ls:
	# 	if i not in garbage:
	# 		for j in garbage:
	# 			if j in i:
	# 				i=i.replace(j,"")
	# 		ans = ans+i
	# 		ans = ans+" "
	# if(len(ans)==0):
	# 	return "Unknown"
	# else:
	# 	return ans
	# st=st.lower()
	for i in garbage:
		if i in st:
			st=st.replace(i,"")
	ls = []
	temp = st.split('_')
	for i in temp:
		ls.extend(i.split(' '))

	ans=""
	for i in ls:
		ans = ans+i
		ans =ans+" "
	if(len(ans)==0):
		ans="Unknown"

	if " er " in ans:
		ans=ans.replace(" er "," Higher ")
	return ans 


# print(remunder("an_ur_aj"))
ar = "raj"
pr = "anuraja"
if ar in pr:
	# print(111)
	pr=pr.replace(ar,"")
print(pr)

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

	rmbl = []
	rmbl.append(itemalbum)
	rmbl.append(itemartist)
	for j in rmbl:
		if j in itemtitle:
			itemtitle=itemtitle.replace(j,"")
	key = itemtitle+itemalbum+itemartist
	if(mp.get(key)):
		continue
	else:
		mp[key]=1
		temptitle=itemtitle.replace(" ","")
		if temptitle=="":
			itemtitle="Title Track"
		if(len(itemalbum)==0):
			itemalbum="Unknown"
		if(len(itemartist)==0):
			itemartist="Unknown"
		num = random.randint(1,10)
		if(i%num==0):
			print(itemtitle," --- ",itemalbum,"---", itemartist)

		print(itemlink)
		if len(itemlink)<200:
			tempsong = Songs(songTitle = itemtitle, songAlbum = itemalbum, songSinger= itemartist, link= itemlink)
			tempsong.save()

 