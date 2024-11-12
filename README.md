# Evan_Li_IDS706_Hwk12

[![CI](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk12/actions/workflows/cicd.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk12/actions/workflows/cicd.yml)

## Dataset Overview

The data is sourced from [Kaggle's Data Engineer Salary in 2024 dataset](https://www.kaggle.com/datasets/chopper53/data-engineer-salary-in-2024). This dataset provides insights into data engineer salaries and employment attributes for the year 2024. It includes information such as:
   - Salary
   - Job title
   - Experience level
   - Employment type
   - Employee residence
   - Remote work ratio
   - Company location
   - Company size

## Key Features
1. Uses PySpark SQL for complex queries
2. Implements window functions for advanced analytics
3. Provides comprehensive salary analysis by experience level
4. Generates formatted output in markdown

## Actions

### Preparation:
1. Install all dependencies: `make install`
2. run: `make run`
3. [Pyspark Output Data/Summary Markdown File](analysis_results.md)

### Format code
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`

## PySpark Data Processing
The project implements data processing on a Data Engineer Salary dataset using PySpark. It includes Spark SQL query and data transformation. Here are the key components:

### Data Processing Pipeline
#### 1. Data Loading and Extraction
- Reads salary data from CSV file using PySpark
- Selects relevant columns including work year, experience level, job title, salary, remote ratio, and company size


#### 2. Statistical Analysis
- Calculates descriptive statistics for salaries (count, mean, stddev, quartiles)
- Generates job title distribution analysis
- Analyzes experience level distribution
- Computes salary statistics by experience level

#### 3. Advanced Analytics
- Implements Spark SQL queries to analyze high-paying jobs
- Performs complex data transformations using DataFrame API
- Creates salary range categories and calculates distributions

#### 4. Results Generation
- Outputs results to a markdown file
- Includes statistical summaries and analysis
