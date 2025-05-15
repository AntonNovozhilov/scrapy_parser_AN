import scrapy


class PepParseItem(scrapy.Item):
    """Объект класса Item с описанными полями."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
