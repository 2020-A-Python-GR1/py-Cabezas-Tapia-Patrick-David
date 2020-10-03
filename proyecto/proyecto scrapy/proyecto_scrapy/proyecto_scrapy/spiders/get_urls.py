import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class GetUrls(CrawlSpider):
    name = 'arania_games'

    allowed_domains = [
        'gamestorrents.nu'
    ]
 
    start_urls = ['https://www.gamestorrents.nu/tag/etiquetas/']

    for i  in range(2,22): #22 páginas
        start_urls.append(f'https://www.gamestorrents.nu/tag/etiquetas/page/{i}/')

    
    segmentos_url_permitidos = (
        'tag/etiquetas/'
    )

    segmentos_url_restringidos = (
        'pages/detail.jsf'
    )

    rules = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= segmentos_url_permitidos,
                deny=segmentos_url_restringidos,
            ),
            callback= 'parse_page'
        ),
    )

    def parse_page(self,response):

        contenedor = response.xpath('/html/body/div/div/section/ul/div/a').get()
        
        data = str(contenedor).split('"')[3]
        print(data)  
        with open('texto.txt', 'a+', encoding = 'utf-8') as archivo:
            archivo.write('\''+data + '\'\n')
        
            
    
