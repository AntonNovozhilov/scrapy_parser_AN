from pep_parse.constants import LOG_DIR, RES

BOT_NAME = "pep_parse"

NEWSPIDER_MODULE = "pep_parse.spiders"

SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

LOG_FILE = LOG_DIR / "scrapy_log.txt"

LOG_LEVEL = "INFO"

FEEDS = {
    f"{RES}/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    },
}
