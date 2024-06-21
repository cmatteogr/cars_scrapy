"""
Author: Cesar M. Gonzalez R.

Car scrapy Basic data
"""

import json

import scrapy

from car_scrapy.constants import CARS_REST_HEADER, CARS_SEARCH_URL


class CarsCarsBasicSpider(scrapy.Spider):
    """
    Spyder to extract Basic cars data
    """
    # Init spyder variables
    name = 'cars_cars_spider'
    offsets_n = 0  # Offset used to limit the pagination when it doesn't end and always return values
    offsets_threshold = 300000  # Offset threshold. Define the amount of data to extract if pagination doesn't end
    page = 0  # Page counter

    def start_requests(self):
        # Queue the request, Cars basic data
        yield scrapy.Request(CARS_SEARCH_URL.format(page=self.page), method='GET', body=None, headers=CARS_REST_HEADER)

    def parse(self, response):
        # Find the script tag which includes 'itemListElement' where is located the car data  in JSON format
        script = response.xpath('//script[contains(text(), "itemListElement")]/text()').get()

        # If tag is found (cars data)
        if script:
            # Strip any leading/trailing whitespace that might affect json parsing
            cleaned_script = script.strip()
            # Parse the JSON data from the script content
            cars_data = json.loads(cleaned_script)
            # Filter items 
            items_cars_data = cars_data['itemListElement']
            # For each item yield the element. Save them in the items.json file
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
                yield scrapy.Request(CARS_SEARCH_URL.format(page=self.page), method='GET', body=None,
                                     headers=CARS_REST_HEADER)

    def handle_error(self, failure, car_url):
        # Handle request failure
        print(f'Request failed: {failure}', {car_url})
