import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' # Heredado
    print('\nlol\n')
    allowed_domains = [ # Heredado
        'un.org'
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' # Nombre funcion a ejecutar para parsear 
        ),
        # segundo parametro vacio
    )

    

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ), callback='parse_page'
        ),
        # Parametro Vacio
    )


    url_segmento_restringido = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    ## Busca dentro de los dominios permitidos y los segmentos permitidos
    ## y en los segmentos no permitidos
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = url_segmento_restringido
            ), callback = 'parse_page'
        ),
    )



    rules = regla_tres # Heredada

    def parse_page(self, response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+', encoding = 'utf-8') as archivo:
                archivo.write(agencia + '\n')
