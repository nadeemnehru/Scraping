import scrapy

class FreshersWorld(scrapy.Spider):
	name = "skillsBot"
	
	start_urls = ["https://www.freshersworld.com/jobs-by-skills"]

	def parse(self, response):
		pageClass = response.selector.xpath('//div[@class = "col-md-4 col-lg-4 col-xs-4 margin-top-20 bold_elig"]/a/@href').extract()
		for Class in pageClass:
			nextPage = "https://www.freshersworld.com" + Class
			yield scrapy.Request(url = nextPage, callback = self.parseClass)

	def parseClass(self, response):
		pages = response.selector.xpath('//div[@class = "col-md-12 col-xs-12 col-lg-12 padding-none left_move_up_new"]/a/@href').extract()
		for page in pages:
			yield scrapy.Request(url = page, callback = self.parseSkills)


	def parseSkills(self, response):
		key = response.selector.xpath('//span[@class = "latest-jobs-title font-18"]/text()').extract()[0]
		value = response.selector.xpath('//span[@class="eligibility-skills display-block modal-open"]/span[@class="elig_pos"]/a/text()').extract()
		yield {key: value}	

