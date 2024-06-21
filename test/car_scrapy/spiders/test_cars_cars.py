"""
Test Cars Spiders
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging

from car_scrapy.spiders.cars_cars_basic import CarsCarsBasicSpider
from scrapy.utils.project import get_project_settings

from car_scrapy.spiders.cars_cars_details import CarsCarsDetailsSpider


def test_cars_basic_spyder():
    # Configure the logs print
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

    # Init the spyder settings
    settings_basic = get_project_settings()
    settings_basic.set('ITEM_PIPELINES', {'car_scrapy.pipelines.CollectAllCarsPipeline': 100})
    # Start the spyder execution. Basic cars extraction
    process = CrawlerProcess(settings_basic)
    process.crawl(CarsCarsBasicSpider)
    process.start()


def test_cars_detailed_spyder():
    # Configure the logs print
    configure_logging({'LOG_FORMAT': '%(levelname)s: %( )s'})

    # Init the spyder settings
    settings_detailed = get_project_settings()
    settings_detailed.set('ITEM_PIPELINES', {'car_scrapy.pipelines.DetailedCarPipeline': 100})
    settings_detailed.set('DOWNLOAD_DELAY', 0.225)  # Set Download delay to avoid webpage banned
    # Start the spyder execution. Detailed cars extraction
    process = CrawlerProcess(settings_detailed)
    process.crawl(CarsCarsDetailsSpider)
    process.start()
