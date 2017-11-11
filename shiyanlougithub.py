import scrapy
class shiyanlougithub(scrapy.Spider):
    name='shiyanlou_github'
    def start_requests(self):
        url_tmpl='https://github.com/shiyanlou?tab=repositories'
        urls=(url_tmpl.format(i) for i in range(1,109))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for re in response.css('div#user-repositories-list li'):
            yield{
                    'name':re.css('h3 a::text,span.mr-3::text').re('\s\w+\-?\w*\-?\w+'),
                    'update_time':re.css('relative-time::attr(datetime)').extract()
                    }
            pass
