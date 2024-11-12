# Evan_Li_IDS706_Hwk12

[![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week10/actions/workflows/cicd.yml)

## PySpark Data Processing
The project involves utilizing PySpark for data processing on a substantial dataset. The main objectives are to incorporate a Spark SQL query and execute a data transformation. I use fivethirtyeight's dataset on showhost guests to peform these operatons. 

### Preparation:
1. open codespaces
2. wait for environment to be installed
3. run: `python main.py`
4. [Pyspark Output Data/Summary Markdown File](pyspark_output.md)

### Format code
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

### Process
1. I first extract the dataset via `extract` 
2. I then start a spark session via `start_spark`
3. I then load the dataset via `load_data`
4. I then find some descriptive statistics via `descibe`
5. I then query the dataset via `query`
6. I then do some more transformation on the sample dataset via `example_transform`
7. I finally end my spark session via `end_spark`

## References
1. https://github.com/nogibjj/python-ruff-template
2. https://github.com/fivethirtyeight/data/tree/master/daily-show-guests



test github actions
