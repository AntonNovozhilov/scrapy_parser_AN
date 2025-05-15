import logging

from pep_parse.constants import RESULT_DIR, TIME


class PepParsePipeline:
    """Описываем класс Pipeline."""

    def __init__(self):
        self.status_dict = {}

    def open_spider(self, spider):
        """Метод нужен по тестам, пока не используется"""
        pass

    def process_item(self, item, spider):
        """Обязательный метод, заполняем и считаем ключи в словаре."""
        status = item["status"]
        if status not in self.status_dict:
            self.status_dict.setdefault(status, 0)
        self.status_dict[status] += 1
        return item

    def close_spider(self, spider):
        """Задаем директорию куда сохранить файл с данными."""
        file_path = RESULT_DIR / f"status_summary_{TIME}.csv"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Статус,Количество\n")
            for status, count in self.status_dict.items():
                f.write(f"{status}, {count}\n")
            f.write(f"Total,{sum(self.status_dict.values())}\n")
            logging.info("Файл создан.")
