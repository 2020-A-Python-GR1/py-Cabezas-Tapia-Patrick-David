# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exception import DropItem

class SoloCapsulasPipeline(object):
    def process_item(self, item, spider):
        titulo = item['titulo']
        if('capsula' no in titulo):
            raise DropItem('No tiene capsula')
        else:
            return item

class TransformarTituloAMonusculas(object):
    def process_item(self,item,spider):
        titulo = item['titulo']
        item['titulo'] = titulo.lower()
        return item

class AraniaFybecaPipeline:
    def process_item(self, item, spider):
        return item
