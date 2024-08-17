#Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
#Нужно взять название источника освещения, цену и ссылку
#Можно попробовать сделать это на другом сайте с продажей источников освещения


import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/nizhny-novgorod/category/svet"]

    def parse(self, response):
        lamps = response.css('div.WdR1o')
        for lamp in lamps:
            yield{
                'name': lamp.css('div.wYUX2 span::text').get(),
                'price': lamp.css('div.q5Uds span::text').get(),
                'link': lamp.css('link::attr(href)').get()
            }

class OzonnewparsSpider(scrapy.Spider):
    name = "Ozonnewpars"
    allowed_domains = ["https://www.ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/osveshchenie-15096"]

    def parse(self, response):
        lamps_ozon = response.css('div.mj5_23')
        for lamp_ozon in lamps_ozon:
            yield {
                'name': lamp_ozon.css('div.x2 span::text').get(),
                'price': lamp_ozon.css('div.c3013-a0 span::text').get().replace("\u2009","").replace("₽",""),
                'link': "https://www.ozon.ru" + lamp_ozon.css('a::attr(href)').get()
            }

