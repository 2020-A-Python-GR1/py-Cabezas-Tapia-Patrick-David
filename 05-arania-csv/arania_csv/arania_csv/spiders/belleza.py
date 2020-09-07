import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):    
    name = 'fybeca'
    # urls = ['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25000']
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=445&s=0&pp=10000'
    ]
    # print(urls)
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'ul.products-list'
        )
        print('\nlol\n')
        precios_normales_sin_formatear = etiqueta_contenedora.css('li > div.product-tile-inner > div.detail > div.side > div.price::attr(data-bind)').extract()
        precios_afiliado_sin_formatear = etiqueta_contenedora.css('li > div.product-tile-inner > div.detail > div.side > div.price-member > div::attr(data-bind)').extract()
        nombre_productos = etiqueta_contenedora.css('li.product-tile::attr(data-name)').extract()

        removetable = str.maketrans('', '', "text:'$' + (")
        precios_normales_sin_formatear = [s.translate(removetable) for s in precios_normales_sin_formatear]
        precios_normales_sin_formatear = [s.replace(")", " ") for s in precios_normales_sin_formatear]
        precios_normales_sin_formatear = [s.replace("formaMony", " ") for s in precios_normales_sin_formatear]
        precios_normales = [s[0:5].strip() for s in precios_normales_sin_formatear]

        precios_afiliado_sin_formatear = [s.translate(removetable) for s in precios_afiliado_sin_formatear]
        precios_afiliado_sin_formatear = [s.replace(")", " ") for s in precios_afiliado_sin_formatear]
        precios_afiliado_sin_formatear = [s.replace("formaMony", " ") for s in precios_afiliado_sin_formatear]
        precios_afiliado = [s[0:5].strip() for s in precios_afiliado_sin_formatear]

        precio_max = 0
        i_max = 0
        precio_min = 10000000000
        i_min = 0
        suma_normales = 0
        suma_afiliados = 0

        for i in range(len(precios_normales)):

            suma_normales = suma_normales + float(precios_normales[i])

            if(float(precios_normales[i]) > precio_max):
                precio_max = float(precios_normales[i])
                i_max = i
            
            if(float(precios_normales[i]) < precio_min):
                precio_min = float(precios_normales[i])
                i_min = i

        for precio in precios_afiliado:
            suma_afiliados = suma_afiliados + float(precio)
        
        print("\nEl item con maximo precio es: "+nombre_productos[i_max]+" con un precio de "+str(precio_max)+"\n")
        print("\nEl item con minimo precio es: "+nombre_productos[i_min]+" con un precio de "+str(precio_min)+"\n")
        print("\nLa suma de precios normales es de: "+str(round(suma_normales,2))+"\n")
        print("\nLa suma de precios como afiliado es de: "+str(round(suma_afiliados,2))+"\n")
        print("\nEl ahorro al comprar todo como afiliado es de: "+str(round(suma_normales - suma_afiliados, 2))+"\n")

        for nombre in nombre_productos:
            with open('articulos_belleza.txt', 'a+', encoding='utf-8') as archivo:
                archivo.write(nombre + '\n')
        print('\nlol\n')