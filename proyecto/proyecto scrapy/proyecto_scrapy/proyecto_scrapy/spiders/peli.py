import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class PeliSpider(CrawlSpider):
    name = 'arania_mod'
    start_urls = [
        'https://repelis24.co/'
    ]
    for i  in range(1,3): #124 páginas
        start_urls.append('https://repelis24.co/pelicula/page/{i}/'.format(i=i))
    segmentos_url_permitidos = (
        'pelicula\/.*'
    )
    allowed_domains = [
        'repelis24.co'
    ]
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),
            callback = 'parse'
        ),
    )
    rules = regla_dos
    movie_name = []
    release_date = []
    country = []
    runtime = []
    rating = []
    genre = []
    imdb_rating = []
    imdb_votes = []
    tmdb_rating = []
    tmdb_votes = []
    def parse(self,response):
        info = response.css('div.sbox > div.custom_fields > span.valor').extract()
        main_info = response.css('div.content > div.sheader > div.data > div.extra')
        movie_name = info[0].split('>')[1].split('<')[0]
        if('&amp;' in movie_name):
            movie_name = movie_name.replace('&amp;','&')
        self.movie_name.append(movie_name)
        if(len(info)==3):
            imdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
            self.imdb_rating.append(imdb_rating)
            imdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
            self.imdb_votes.append(imdb_votes)
            tmdb_rating = info[2].split('<strong>')[1].split('</strong>')[0]
            self.tmdb_rating.append(tmdb_rating)
            tmdb_votes = info[2].split('</strong>')[1].split('votos')[0].strip()
            if('</span>' in tmdb_votes):
                self.tmdb_votes.append("")
            else:
                self.tmdb_votes.append(tmdb_votes)
        elif(len(info)==2):
            if("repimdb" in info[1]):
                imdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
                self.imdb_rating.append(imdb_rating)
                imdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
                self.imdb_votes.append(imdb_votes)
                self.tmdb_rating.append("")
                self.tmdb_votes.append("") 
            else:
                tmdb_rating = info[1].split('<strong>')[1].split('</strong>')[0]
                self.tmdb_rating.append(tmdb_rating)
                tmdb_votes = info[1].split('</strong>')[1].split('votos')[0].strip()
                if('</span>' in tmdb_votes):
                    self.tmdb_votes.append("")
                else:
                    self.tmdb_votes.append(tmdb_votes)
                self.imdb_rating.append("")
                self.imdb_votes.append("")
        else:
            self.tmdb_rating.append("")
            self.tmdb_votes.append("")
            self.imdb_rating.append("")
            self.imdb_votes.append("")

        if(main_info.css('span.date::text').extract()):
            release_date = main_info.css('span.date::text').extract()[0]
            self.release_date.append(release_date)
        else:
            self.release_date.append("")
        if(main_info.css('span.country::text').extract()):
            country = main_info.css('span.country::text').extract()[0]
            self.country.append(country)
        else:
            self.country.append("")
        if(main_info.css('span.runtime::text').extract()):
            runtime = main_info.css('span.runtime::text').extract()[0]
            self.runtime.append(runtime)
        else:
            self.runtime.append("")
        if(main_info.css('span.rated::text').extract()):
            rating = main_info.css('span.rated::text').extract()[0]
            self.rating.append(rating)
        else:
            self.rating.append("")
        if(response.css('div.sgeneros > a::text').extract()):
            genre = response.css('div.sgeneros > a::text').extract()[0]
            self.genre.append(genre)
        else:
            self.genre.append("")

    def closed( self, reason ):
        save_path = './movies.csv'
        df = pd.DataFrame(
            {
                'movie_name': pd.Series(self.movie_name),
                'release_date': pd.Series(self.release_date),
                'country': pd.Series(self.country),
                'runtime': pd.Series(self.runtime),
                'rating': pd.Series(self.rating),
                'genre': pd.Series(self.genre),
                'imdb_rating': pd.Series(self.imdb_rating),
                'imdb_votes': pd.Series(self.imdb_votes),
                'tmdb_rating': pd.Series(self.tmdb_rating),
                'tmdb_votes': pd.Series(self.tmdb_votes)
            }
        )
        df.to_csv(save_path,index=False)
