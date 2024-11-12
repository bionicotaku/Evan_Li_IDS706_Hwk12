import pytest
from mylib.calculate_stat import (
    read_data,
    calculate_salary_stats_by_experience,
)
from pyspark.sql import SparkSession, DataFrame


@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder.appName("TestSalaryAnalysis")
        .master("local[*]")
        .getOrCreate()
    )


@pytest.fixture
def sample_data(spark):
    return spark.createDataFrame(
        [
            (2020, "EN", "Data Analyst", 50000, 0, "S"),
            (2021, "MI", "Software Engineer", 75000, 50, "M"),
            (2022, "SE", "Data Scientist", 100000, 100, "L"),
            (2023, "EX", "Manager", 150000, 100, "L"),
        ],
        [
            "work_year",
            "experience_level",
            "job_title",
            "salary_in_usd",
            "remote_ratio",
            "company_size",
        ],
    )


def test_read_data(tmp_path, spark):
    # Create test data directly as Spark DataFrame
    test_data = spark.createDataFrame(
        [
            (2020, "EN", "Data Analyst", 50000, 0, "S"),
            (2021, "MI", "Software Engineer", 75000, 50, "M"),
        ],
        [
            "work_year",
            "experience_level",
            "job_title",
            "salary_in_usd",
            "remote_ratio",
            "company_size",
        ],
    )

    # Write test data to CSV
    file_path = str(tmp_path / "test.csv")
    test_data.write.csv(file_path, header=True, mode="overwrite")

    # Test reading the data
    result = read_data(file_path)
    assert isinstance(result, DataFrame)
    assert set(result.columns) == {
        "work_year",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_size",
    }


def test_calculate_salary_stats_by_experience(sample_data):
    result = calculate_salary_stats_by_experience(sample_data)
    assert isinstance(result, DataFrame)

    # Convert to pandas for easier assertion
    result_pd = result.toPandas()
    assert set(result_pd["experience_level"]) == {"EN", "EX", "MI", "SE"}
    assert all(
        col in result_pd.columns
        for col in ["experience_level", "mean", "median", "min", "max"]
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
