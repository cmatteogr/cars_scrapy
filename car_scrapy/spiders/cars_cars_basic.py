"""
Author: Cesar M. Gonzalez R.

Car scrapy Basic data
"""

import scrapy
import json
from car_scrapy.constants import CARS_REST_HEADER, CARS_SEARCH_URL


class CarsCarsBasicSpider(scrapy.Spider):
    name = 'cars_cars_spider'
    offsets_n = 0
    offsets_threshold = 300000
    page = 0

    def start_requests(self):
        # Queue the request, include callback arguments locations_fr to count the offset
        yield scrapy.Request(CARS_SEARCH_URL.format(page=self.page), method='GET', body=None, headers=CARS_REST_HEADER)

    def parse(self, response):
        # Find the script tag that includes 'itemListElement' in its JSON content
        script = response.xpath('//script[contains(text(), "itemListElement")]/text()').get()

        if script:
            # Strip any leading/trailing whitespace that might affect json parsing
            cleaned_script = script.strip()
            # Parse the JSON data from the script content
            cars_data = json.loads(cleaned_script)
            # Filter items 
            items_cars_data = cars_data['itemListElement']
            # For each item yield the element
            for item_cars_data in items_cars_data:
                # Process or yield the data
                yield item_cars_data

            # Count extracted items and sum with total offset
            self.offsets_n += len(items_cars_data)
            # End spyder if threshold was reached
            if len(items_cars_data) == 0 or self.offsets_n > self.offsets_threshold:
                print("There aren't records in list or offset threshold was reached")
            else:
                # Increase page, get data from following page
                self.page += 1
                yield scrapy.Request(CARS_SEARCH_URL.format(page=self.page), method='GET', body=None, headers=CARS_REST_HEADER)

    def handle_error(self, failure, car_url):
        # Handle request failure
        print(f'Request failed: {failure}', {car_url})
