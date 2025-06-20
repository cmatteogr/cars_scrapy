"""
Author: Cesar M. Gonzalez R
Repository layer.
Mongo DB Repository
"""
import abc

from car_scrapy.constants import MONGODB_FULLDATA_COLLECTION_NAME


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_cars(self, query: str, query_filter: dict = None):
        raise NotImplementedError

    @abc.abstractmethod
    def insert_one_car(self, car_obj):
        raise NotImplementedError


class MongoDBRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def get_cars(self, query: str, query_filter: dict = None):
        # Connect with collection and filter by input arguments
        collection = self.session[MONGODB_FULLDATA_COLLECTION_NAME]
        if query_filter:
            return collection.find(query, query_filter)
        return collection.find(query)

    def insert_one_car(self, car_obj):
        # Insert car obj in db
        collection = self.session[MONGODB_FULLDATA_COLLECTION_NAME]
        if not car_obj:
            raise Exception("Cars Obj is empty, review the input argument")
        return collection.insert_one(car_obj)
