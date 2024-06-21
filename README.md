# Cars Scrapy - A Template to Extract data from Internet
  ![Long term parking, art by Arman](https://github.com/cmatteogr/cars_scrapy/assets/138587358/529414f6-1856-4972-bc03-f57ac914eb88)

Cars Scrapy is a project build in Medellin Machine Learning - Study Group (MML-SG) used as template to extract data from internet. This project extracts data from a cars portal but it can be extended to any other "conventional" web portal

## Requirements
* Install Python 3.10 or higher.
* Install the libraries using requirements.txt.
* Setup MongoDB or the repository connection to have access to desired storage resource.

## Usage
Two scripts were developed to extract the data, they are located in the **test** folder:
* test_cars_cars: Contains the test cases to extract basic an detailed cars data. Use test_cars_basic_spyder first to extract basic data and then test_cars_detailed_spyder to extract detailed data.
* test_data_extraction: Used to export data from repository (MongoDB) to a CSV file.

**WARNING**: Be careful using the extraction scripts, you can be banned or the web portal could add access restrictions.
