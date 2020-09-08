import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FybecaCrawl(CrawlSpider):
    name = 'arania_fybeca'

    allowed_domains = [
        'fybeca.com'
    ]

    numero = '10000'
 
    start_urls=[
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp={numero}',
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp={numero}',
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp={numero}',
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp={numero}',
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp={numero}',
        f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=457&s=0&pp={numero}'
    ]
    segmentos_url_permitidos = (
        f'cat=446&s=0&pp={numero}',
        f'cat=537&s=0&pp={numero}',
        f'cat=446&s=0&pp={numero}',
        f'cat=489&s=0&pp={numero}',
        f'cat=562&s=0&pp={numero}',
        f'cat=457&s=0&pp={numero}'
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

        contenedor = response.css(
            'div.product-tile-inner'
        )
        
        productos = list(contenedor.css(
            "a.name::text"
        ).extract())
        
        precios = list(contenedor.css(
            "div.detail > div.side > div.price::attr(data-bind)"
        ).extract())

        precios_afiliados = list(contenedor.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
        ).extract())

        lista_precios = []
        for i in precios:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            lista_precios.append(precio)      

        lista_precios_afiliados = []
        for i in precios_afiliados:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            lista_precios_afiliados.append(precio)


        maximo_afiliado = max(lista_precios_afiliados)
        minimo_afiliado = min(lista_precios_afiliados)
        maximo = max(lista_precios)
        minimo = min(lista_precios)
        producto_max = productos[lista_precios.index(maximo)]
        producto_min = productos[lista_precios.index(minimo)]
        
        print("Producto mas barato:", producto_min ,'con un precio de', minimo,'$,','ahorro', minimo-minimo_afiliado,'$')  
        print("Producto mas costoso:", producto_max ,'con un precio de', maximo,'$,','ahorro', maximo-maximo_afiliado,'$')
        print('Sen encontraron',len(productos),'productos')
        print("\n\n")        

        for i in productos:        
            with open('belleza.txt', 'a+', encoding = 'utf-8') as archivo:
                archivo.write(i + '\n')
        
            
    

