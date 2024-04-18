"""
Author: Cesar M. Gonzalez

Data extraction from repository
"""

import pandas as pd


# THIS METHOD CAN BE IMPROVED
def extract_car_model_data(uow, query: {}) -> pd.DataFrame:
    """
    Extract cars data from repository and transform to a tabular data
    :param uow: Unit of work
    :param query: DB query
    :return: Tabular data Dataframe
    """
    # Connect with repository and get car data
    with uow:
        cars = uow.repo.get_cars(query)

        # Filter relevant data used to train the ML model
        cars_info = list(
            map(lambda x: [x['msrp'],
                           x['year'],
                           x['canonical_mmty'],
                           x['model'],
                           x['local_zone'],
                           x['interior_color'],
                           x['aff_code'],
                           x['price'],
                           x['price_badge'],
                           x['trim'],
                           x['drivetrain'],
                           x['dealer_name'],
                           x['dealer_zip'],
                           x['mileage'],
                           x['make'],
                           x['bodystyle'],
                           x['cat'],
                           x['vin'],
                           x['canonical_mmt'],
                           x['fuel_type'],
                           x['stock_type'],
                           x['exterior_color'],
                           x['page_channel']],
                cars))

        columns_names = ['msrp', 'year', 'canonical_mmty', 'model', 'local_zone', 'interior_color', 'aff_code', 'price',
                         'price_badge', 'trim', 'drivetrain', 'dealer_name', 'dealer_zip', 'mileage', 'make',
                         'bodystyle', 'cat', 'vin', 'canonical_mmt', 'fuel_type', 'stock_type', 'exterior_color',
                         'page_channel']
        # Return tabular real state data
        df = pd.DataFrame(cars_info, columns=columns_names)
        return df
