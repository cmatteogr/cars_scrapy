"""
Test Cars Spiders
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging

from car_scrapy.spiders.cars_cars_basic import CarsCarsBasicSpider
from scrapy.utils.project import get_project_settings

from car_scrapy.spiders.cars_cars_details import CarsCarsDetailsSpider


def test_cars_basic_spyder():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

    settings_basic = get_project_settings()
    settings_basic.set('ITEM_PIPELINES', {'car_scrapy.pipelines.CollectAllCarsPipeline': 100})
    process = CrawlerProcess(settings_basic)
    process.crawl(CarsCarsBasicSpider)
    process.start()


def test_cars_detailed_spyder():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

    settings_detailed = get_project_settings()
    settings_detailed.set('ITEM_PIPELINES', {'car_scrapy.pipelines.DetailedCarPipeline': 100})
    process = CrawlerProcess(settings_detailed)
    process.crawl(CarsCarsDetailsSpider)
    process.start()
