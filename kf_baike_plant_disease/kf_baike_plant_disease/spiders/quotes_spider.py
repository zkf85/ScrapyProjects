import scrapy
import os

class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    disease_name_list_file = 'list_for_scrapy.txt'
    with open(disease_name_list_file, 'r') as f:
        item_list = f.read().split()

    item_list = [x.replace(',','') for x in item_list]
    #item_list = [x.split(',')[1] for x in item_list]

    print(item_list)

    def start_requests(self):
        base_url = 'https://baike.baidu.com/item'
        
        for item in self.item_list:
            yield scrapy.Request(url=os.path.join(base_url, item), callback=self.parse)


    def parse(self, response):
        filename = '%s.html' % ''.join(response.css('title::text').extract())
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
