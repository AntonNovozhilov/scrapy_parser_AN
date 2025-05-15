import re
import scrapy
import logging

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Класс описывающий паука."""

    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """Парсим ссылки на документы PEP и применяем к каждой parse_pep()."""
        logging.info("Парсер начал работу.")
        pep_links = response.css("tr td:nth-child(2) a[href]")
        for pep_link in pep_links:
            if pep_link:
                yield response.follow(pep_link, callback=self.parse_pep)
            else:
                logging.info("Ссылка не найдена.")
        logging.info("Парсер закончил свою работу.")

    def parse_pep(self, response):
        """Парсим информацию с страницы PEP и записываем ее в объект Item."""
        item = PepParseItem()
        item["number"] = re.search(
            r"PEP (\d+)", response.css("h1.page-title::text").get().strip()
        ).group(1)
        item["name"] = response.css("h1.page-title::text").get().strip()
        item["status"] = response.css("abbr::text").get().strip()
        yield item
