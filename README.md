# Cars Scrapy - A Template to Extract data from Internet
  ![Long term parking, art by Arman](https://github.com/cmatteogr/cars_scrapy/assets/138587358/529414f6-1856-4972-bc03-f57ac914eb88)

Cars Scrapy is a project build in Medellin Machine Learning - Study Group (MML-SG) used as template to extract data from internet. This project extracts data from a cars portal but it can be extended to any other "conventional" web portal

## Prerequisites
* Install Python 3.10 or higher.
* Install the libraries using requirements.txt.
```bash
pip install -r requirements.txt
```
* Setup MongoDB or the repository connection to have access to desired storage resource.

## Usage
Two scripts were developed to extract the data, they are located in the **test** folder:
* test_cars_cars: Contains the test cases to extract basic an detailed cars data. Use test_cars_basic_spyder first to extract basic data and then test_cars_detailed_spyder to extract detailed data.
* test_data_extraction: Used to export data from repository (MongoDB) to a CSV file.

**WARNING**: Be careful using the extraction scripts, you can be banned or the web portal could add access restrictions.

## External Resources
This project was built by the Medellín Machine Learning - Study Group (MML-SG) community. In the following [link](https://drive.google.com/drive/u/0/folders/1nPMtg6caIef5o9S_J8WyNEvyEt5sO1VH) you can find the meetings records about it:
* [2. Exploración de Modelos de ML y Exploración de Datos (2024-02-28 19:14 GMT-5)](https://drive.google.com/file/d/1mqpccGVjhOQTDV5c80RKk1ECNnK6DCqn/view?usp=drive_link)
* [3. Análisis de Datos y Selección de Variables para Modelado (2024-03-06 19:08 GMT-5)](https://drive.google.com/file/d/1N9LrEJ3TYRZY6Fumxor3HircIahtwM24/view?usp=drive_link)
* [4. Construcción del Modelo de Predicción - Supervised Learning(2024-03-13 19:07 GMT-5)](https://drive.google.com/file/d/1PgFWmeBnIu__lHYkYQ4wIvJzyWro0tXM/view?usp=drive_link)
