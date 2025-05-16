import csv
import logging
from collections import Counter

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
        data = (
            ("Статус", "Количество"),
            *self.status_dict.items(),
            ("Total", sum(self.status_dict.values()))
        )
        with open(self.file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        logging.info("Файл создан.")
