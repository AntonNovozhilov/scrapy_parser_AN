import csv
from collections import Counter
import logging

from pep_parse.constants import RESULT_DIR, TIME


class PepParsePipeline:
    """Описываем класс Pipeline."""

    def __init__(self):
        self.file_path = RESULT_DIR / f"status_summary_{TIME}.csv"

    def open_spider(self, spider):
        """Метод нужен по тестам, пока не используется"""
        self.status_dict = Counter()

    def process_item(self, item, spider):
        """Обязательный метод, заполняем и считаем ключи в словаре."""
        status = item["status"]
        self.status_dict[status] += 1
        return item

    def close_spider(self, spider):
        """Задаем директорию куда сохранить файл с данными."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Статус", "Количество"])
            writer.writerows(self.status_dict.items())
            writer.writerow(["Total", sum(self.status_dict.values())])
        logging.info("Файл создан.")
