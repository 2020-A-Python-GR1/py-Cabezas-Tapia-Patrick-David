import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()

        print('Precio')
        precio_completo = response.css('div.product_price')
        precio = precio_completo.css('p.price_color::text').extract()
        print(precio)
        productos = []
        for item in precio:
                productos.append(item.replace('£',''))
        print(productos)
        print()
        
        print('Elementos del stock')
        stock = precio_completo.css('p.instock::text').extract()
        for item in stock:
            print(item.replace('\n',''))
        
        print()
        print('Estrellas ')
        estrellas = response.css('p.star-rating').extract()
        for i in estrellas:
            print(i.partition('\n')[0].split('rating')[1].split('\"')[0])