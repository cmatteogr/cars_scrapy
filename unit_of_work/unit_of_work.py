"""
Author: Cesar M. Gonzalez R.

Units of Work
"""

from __future__ import annotations

import abc

import pymongo

import config
from adapters import repository


class AbstractUnitOfWork(abc.ABC):
    """
    Abstract class that defines the interface for all units of work.
    """
    repo: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        # self.rollback()
        pass

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError


class MongoDBUnitOfWork(AbstractUnitOfWork):
    """
    Class to define the MongoDB units of work.
    """

    def __init__(self, as_instance=False):
        # If connection is initialized as instance then initialize the repository connection
        self.as_instance = as_instance
        if self.as_instance:
            self.client = pymongo.MongoClient(config.get_mongo_uri())
            self.session = self.client[config.get_database_name()]  # type: Session
            self.repo = repository.MongoDBRepository(self.session)

    def __enter__(self):
        if self.as_instance:
            raise Exception("Connection was Initialized as instance")
        self.client = pymongo.MongoClient(config.get_mongo_uri())
        self.session = self.client[config.get_database_name()]  # type: Session
        self.repo = repository.MongoDBRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.client.close()

    def _commit(self):
        pass

    def close(self):
        if not self.as_instance:
            raise Exception("Connection was not initialized as instance, use 'with' instead")
        self.client.close()
