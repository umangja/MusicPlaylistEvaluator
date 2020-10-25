import scrapy
import json
import pandas as pd
from csv import writer


class bestwap(scrapy.Spider):
	name = "myscrapper"

	def start_requests(self):
		url = "https://bestwap2.in/category/12967/mp3-songs-a709e.html"
		yield scrapy.Request(url = url, callback = self.parseYearList)

	def parseYearList(self, response):

		devs = response.css("div.dev")
		yearlist = devs.css("a::attr(href)").getall()
		yearlist = yearlist[:8]

		
		for url in yearlist:
			yield scrapy.Request(url = url, callback = self.getmovielist)

	def getmovielist(self, response):
		devs = response.css("div.dev")
		movielist = devs.css("a::attr(href)").getall()

		# for i in movielist:
		# 	print(i)
		pattern = "https://bestwap2.in/category/{}/0/abcd/{}.html"

		pageid  = response.url.split('/')[4]

		pageno = response.css("div.pgn::text").get()
		# print(pageno)
		if pageno is None:
			n=1
		else:
			n = int(pageno.split('/')[1].split(')')[0])
		finurls = []
		for i in range(n):
			finurls.append(pattern.format(pageid,i))

		# print(finurls)
		for url in finurls:
			yield scrapy.Request(url = url, callback=self.getmovielist2)


	def getmovielist2(self,response):
		devs = response.css("div.dev")
		movielistfinal = devs.css("a::attr(href)").getall()

		for url in movielistfinal:
			yield scrapy.Request(url = url, callback=self.getsonglist)

	def getsonglist(self,response):
		
		lists = response.css("div.list")

		if len(lists)!=0:
			print("songlist reached")
			songlist = lists.css("a::attr(href)").getall()
			for url in songlist:
				yield scrapy.Request(url = url, callback =self.getstreamlink)
		else:
			print("quality page reached")
			devs = response.css("div.dev")
			quality = devs.css("a::attr(href)").getall()[-1]
			yield scrapy.Request(url = quality, callback = self.afterquality)

		# final.extend(songlist)
		# filename = 'data.json'
		

	def afterquality(self,response):
		print("after quality reached")
		lists = response.css("div.list")
		songlist = lists.css("a::attr(href)").getall()
		for url in songlist:
			yield scrapy.Request(url = url, callback =self.getstreamlink)



	def getstreamlink(self,response):

		link  = response.css("source::attr(src)").get()
		cntr = response.css("b")
		ncnt = cntr.css("a::text").get()


		print("artist name = ",ncnt)

		with open('data.json') as json_file:
			data = json.load(json_file)
		data.append(link+'++'+ncnt)
		with open('data.json', 'w+') as json_file:
			json.dump(data, json_file,indent = 4,sort_keys=True)



