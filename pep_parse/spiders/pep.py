import re
import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('tr td:nth-child(2) a[href]')
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)
        

    def parse_pep(self, response):
        """Docstring"""
        pepnumber = re.search(
            r'PEP (\d+)',
            response.css('h1.page-title::text').get().strip()).group(1)
        yield {
            'number': pepnumber,
            'name': response.css('h1.page-title::text').get().strip(),
            'status': response.css('abbr::text').get().strip(),
        }

