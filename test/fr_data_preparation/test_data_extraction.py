"""
Test data extraction
"""
from car_data_preparation.data_extraction import extract_car_model_data
import pytest

from unit_of_work.unit_of_work import MongoDBUnitOfWork


@pytest.fixture
def uow():
    yield MongoDBUnitOfWork()


def test_data_extraction(uow):
    query = {}
    filepath = r'cars.csv'
    properties_df = extract_car_model_data(uow, query)
    properties_df.to_csv(filepath)

