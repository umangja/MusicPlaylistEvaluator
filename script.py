import json
from evaluate.models import Songs


Songs.objects.all().delete()
with open('data.json') as json_file:
	dat = json.load(json_file)
i=0
for item in dat:
	# print(i)
	i+=1
	itemlink = item.split('++')[0]
	itemartist = item.split('++')[1]
	if itemartist.split(' ')[0]=="Download" or itemartist=='\n' or len(itemartist)>50:
		itemartist="Unknown"
	itemtitle = itemlink.split('/')[-1]
	itemtitle = itemtitle[:-4]
	if len(itemtitle)>50:
		itemtitle=itemtitle[:45]+'...'
	itemalbum = itemlink.split('/')[-2]
	if(itemalbum[0]=='6'):
		itemalbum = itemlink.split('/')[-3]
	if len(itemalbum)>50:
		itemalbum=itemalbum[:45]+'...'
	if len(itemlink)<200:
		tempsong = Songs(songTitle = itemtitle, songAlbum = itemalbum, songSinger= itemartist, link= itemlink)
		tempsong.save()

 