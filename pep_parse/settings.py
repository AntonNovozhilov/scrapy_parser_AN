from pep_parse.constants import LOG_DIR

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]

NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

LOG_FILE = LOG_DIR / "scrapy_log.txt"

LOG_LEVEL = "INFO"

FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    },
}
