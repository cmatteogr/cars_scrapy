"""
Author: Cesar M. Gonzalez R.

Car scrapy Details data
"""
import json
from functools import partial

import scrapy

from car_scrapy.constants import CARS_REST_HEADER2
from car_scrapy.items import CarItem


class CarsCarsDetailsSpider(scrapy.Spider):
    name = 'fr_properties_spider'
    offsets_dict = {}

    def start_requests(self):
        # Open the file and read line by line
        with open("items.jsonl", 'r') as file:
            for line in file:
                # Parse the JSON data in each line
                data = json.loads(line)
                # Get car URL
                car_url = data['url']
                print(f"URL real state details: {car_url}")
                yield scrapy.Request(car_url, method='GET', body=None, headers=CARS_REST_HEADER2,
                                     callback=partial(self.parse, car_url=car_url),
                                     errback=partial(self.handle_error, car_url=car_url))

    def parse(self, response, car_url):
        # Use the xpath selector to find the script tag and extract its contents
        car_json_data = response.xpath('//script[@id="initial-activity-data"]/text()').get()

        # Create the Car Item
        car_item = CarItem()
        car_item['status'] = 'ok'
        car_item['url'] = car_url
        car_item['response'] = json.loads(car_json_data)

        yield car_item

    def handle_error(self, failure, car_url):
        # Handle request failure
        print(f'Request failed: {failure}')
        # Create the Property Item
        car_item = CarItem()
        car_item['status'] = 'error'
        car_item['url'] = car_url
        car_item['response'] = failure

        yield car_item
