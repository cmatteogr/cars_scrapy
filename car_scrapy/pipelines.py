# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from unit_of_work.unit_of_work import MongoDBUnitOfWork


class CollectAllCarsPipeline:
    def __init__(self):
        self.items = []

    def open_spider(self, spider):
        # Init JSONL file
        self.file = open("items.jsonl", "w")

    def close_spider(self, spider):
        # Close File
        self.file.close()

    def process_item(self, item, spider):
        # Write line with data extracted
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item


class DetailedCarPipeline:

    def open_spider(self, spider):
        # Initialize MongoDB connection
        self.m_uow = MongoDBUnitOfWork(as_instance=True)
        # Init failed file
        self.file = open("failed_items.jsonl", "w")

    def close_spider(self, spider):
        # Close DB connection
        self.m_uow.close()
        # Close File
        self.file.close()

    def process_item(self, item, spider):
        # Base on item status save in DB or write URL in file
        request_status = item['status']
        match request_status:
            case 'ok':
                # Insert item into MongoDB
                inserted_document = self.m_uow.repo.insert_one_car(item['response'])
                # Print the ID of the inserted document
                print("Inserted document ID:", inserted_document.inserted_id)
            case _:
                line = json.dumps(item['url']) + "\n"
                self.file.write(line)

        return item
