# -*- coding: utf-8 -*-
import scrapy
import os


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'yola-xpath'
    start_urls = [
        'http://cn.made-in-china.com/',
    ]
        # 'http://quotes.toscrape.com/',

    def parse(self, response):
        for quote in response.xpath('//a'):
            tmp_url = quote.xpath('./@href').extract_first()
            if tmp_url.find("http") < 0:
                tmp_url = os.path.join("http://cn.made-in-china.com" , tmp_url)
                pass
                
            yield {
                'urls': tmp_url
            }

        next_page_url = response.xpath('//a').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


        """
        {'text': 
            u'\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d', 
        'tags': 
            [u'aliteracy', u'books', u'classic', u'humor'], 
        'author': 
            u'Jane Austen'}
2017-11-13 19:35:58 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>
{'text': u"\u201cImperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.\u201d", 'tags': [u'be-yourself', u'inspirational'], 'author':
 u'Marilyn Monroe'}

        """