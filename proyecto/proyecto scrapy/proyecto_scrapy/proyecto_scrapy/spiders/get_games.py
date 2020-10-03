import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class AraniaJuegos(scrapy.Spider):
    name = 'juegos'  # Heredado (override)

    url = [
        'https://www.gamestorrents.nu/juegos/tropico-6-el-prez-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/iron-harvest-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/nba-playgrounds-elamigos/'
        'https://www.gamestorrents.nu/juegos/maid-of-sker-elamigos/'
        'https://www.gamestorrents.nu/juegos/resident-evil-3-2020-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/hearts-of-iron-iv-field-marshal-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/cities-skylines-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/cuphead-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/steel-division-2-total-conflict-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/heavy-rain-elamigos/'
        'https://www.gamestorrents.nu/juegos/tropico-4-collectors-bundle-elamigos/'
        'https://www.gamestorrents.nu/juegos/resident-evil-hd-remaster-biohazard-hd-elamigos/'
        'https://www.gamestorrents.nu/juegos/assassins-creed-brotherhood-complete-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/alien-isolation-complete-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/dishonored-goty-elamigos/'
        'https://www.gamestorrents.nu/juegos/f1-race-stars-elamigos/'
        'https://www.gamestorrents.nu/juegos/the-lord-of-the-rings-the-return-of-the-king-elamigos/'
        'https://www.gamestorrents.nu/juegos/human-fall-flat-elamigos/'
        'https://www.gamestorrents.nu/juegos/killing-floor-2-digital-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/team-sonic-racing-elamigos/'
        'https://www.gamestorrents.nu/juegos/ni-no-kuni-wrath-of-the-white-witch-remastered-elamigos/'
        'https://www.gamestorrents.nu/juegos/resident-evil-3-2020-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/serious-sam-4-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/windbound-elamigos/'
        'https://www.gamestorrents.nu/juegos/tropico-6-el-prez-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/halo-the-master-chief-collection-elamigos/'
        'https://www.gamestorrents.nu/juegos/tropico-6-el-prez-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/superhot-mind-control-delete-elamigos/'
        'https://www.gamestorrents.nu/juegos/spelunky-2-elamigos/'
        'https://www.gamestorrents.nu/juegos/call-of-duty-black-ops-ii-digital-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/drake-hollow-elamigos/'
        'https://www.gamestorrents.nu/juegos/crusader-kings-iii-royal-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/hotshot-racing-elamigos/'
        'https://www.gamestorrents.nu/juegos/wwe-2k-battlegrounds-elamigos/'
        'https://www.gamestorrents.nu/juegos/fairy-tail-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/house-flipper-elamigos/'
        'https://www.gamestorrents.nu/juegos/titanfall-2-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/serious-sam-4-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/castlestorm-ii-elamigos/'
        'https://www.gamestorrents.nu/juegos/drake-hollow-elamigos/'
        'https://www.gamestorrents.nu/juegos/bright-memory-elamigos/'
        'https://www.gamestorrents.nu/juegos/art-of-rally-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/tropico-6-el-prez-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/art-of-rally-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/kandagawa-jet-girls-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/left-4-dead-2-elamigos/'
        'https://www.gamestorrents.nu/juegos/tropico-6-el-prez-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/resident-evil-3-2020-deluxe-edition-elamigos/'
        'https://www.gamestorrents.nu/juegos/drake-hollow-elamigos/'
        'https://www.gamestorrents.nu/juegos/18-wheels-of-steel-extreme-trucker-2-elamigos/'
        'https://www.gamestorrents.nu/juegos/command-and-conquer-3-tiberium-wars-complete-collection-elamigos/'
        ]

    start_urls = ['https://www.gamestorrents.nu/tag/etiquetas/']

    titulos = []
    fechas = []
    uploaders = []
    tamanios = []
    vistas = []
    votos = []
    ratings = []
    years = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        titulo = response.css('header.Top > h1.Title::text').get()
        self.titulos.append(titulo)

        fecha = response.css(
            'header.Top > div.Info > span.Date::text').get()
        self.fechas.append(fecha)

        uploader = response.css('header.Top > div.Info > span.Qlty::text').get()
        self.uploaders.append(uploader)

        tamanio = response.css(
            'header.Top > div.Info > span.Time::text').get()
        self.tamanios.append(tamanio)

        visitas = response.css(
            'header.Top > div.Info > span.Views::text').get()

        calificaciones = response.css(
            'div.post-ratings > strong::text').extract()
        calificaciones[1] = calificaciones[1].replace(',','.')

        self.votos.append(calificaciones[0])
        self.ratings.append(calificaciones[1])

        visitas = visitas.replace(' visitas', '')
        visitas = visitas.replace('.','')
        self.vistas.append(visitas)

        fechaCompleta = datetime.strptime(fecha, '%d/%m/%y')
        self.years.append(fechaCompleta.year)

        serie_titulo = pd.Series(self.titulos)
        serie_fecha = pd.Series(self.fechas)
        serie_anios = pd.Series(self.years)
        serie_uploader = pd.Series(self.uploaders)
        serie_tamanio = pd.Series(self.tamanios)
        serie_visitas = pd.Series(self.vistas)
        serie_votos = pd.Series(self.votos)
        serie_ratings = pd.Series(self.ratings)
        
        path_guardado = './proyecto_scrapy/lista.csv'

        df = pd.DataFrame({'Titulo': serie_titulo,
                           'Votos': serie_votos,
                           'Rating': serie_ratings,
                           'fecha': serie_fecha,
                           'Anios': serie_anios,
                           'Uploader': serie_uploader,
                           'Tamanio': serie_tamanio,
                           'vistas': serie_visitas})
        df.to_csv(path_guardado,index=False)