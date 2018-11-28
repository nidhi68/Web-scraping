# -*- coding: utf-8 -*-
import scrapy


class IphonesSpider(scrapy.Spider):
    #name of the spider
    name = 'iphones'

    #starting url
    start_urls = ['https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphones']
    
    #location of csv file
    custom_settings={
        'FEED_URI':'tmp/iphones.csv'
    }
    
    
    def parse(self, response):
         #Extracting features of iphones
        title=response.xpath("//a/h2/text()").extract()
        MP=response.xpath("//span[@class='a-size-small a-color-secondary a-text-strike']/text()").extract()
        Discount=response.xpath("//span[@class='a-size-small a-color-price']/text()").extract()
        SP=response.xpath("//span[@class='a-size-base a-color-price s-price a-text-bold']/text()").extract()
        Ratings=response.xpath("//i[@class='a-icon a-icon-star a-star-4']/span/text()").extract()
        
        for item in zip(title,MP,Discount,SP,Ratings):
            scraped_info={
                'Title':item[0],
                'MP':item[1],
                'Discount':item[2],
                'SP':item[3],
                'Ratings':item[4],
            }
            yield scraped_info
        next_page_url=response.xpath("//span[@class='pagnLink']/a/@href").extract_first()
        if next_page_url:
            url=response.urljoin(next_page_url)
            yield scrapy.Request(url=url,callback=self.parse)
        
        
        
