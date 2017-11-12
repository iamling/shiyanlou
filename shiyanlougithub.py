#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy
class shiyanlougithub(scrapy.Spider):
    name='shiyanlou_github'
    def start_requests(self):
        url_tmpl='https://github.com/shiyanlou?tab=repositories'
        urls=(url_tmpl.format(i) for i in range(1,5))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for re in response.css('div#user-repositories-list li.public'):
            yield{
                    'name':re.css('h3 a::text').re_first("\s\w+\-?\w*\-?\w+"),
                    'update_time': re.xpath('.//relative-time/@datetime').extract_first()
                    }
