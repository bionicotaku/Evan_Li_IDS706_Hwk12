from mylib import calculate_stat
from mylib import generate_markdown
import io
from contextlib import redirect_stdout
from pyspark.sql import SparkSession


def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("SalaryAnalysis").getOrCreate()

    try:
        # Read data
        filteredData = calculate_stat.read_data("data/Dataset-salary-2024.csv")

        # Calculate and print statistics
        print("Salary Statistics:")
        calculate_stat.calculate_stat(filteredData).show()
        print()

        # Print job title distribution
        print("Top 20 Job Titles Distribution:")
        calculate_stat.get_job_title_distribution(filteredData).show()
        print()

        # Print experience level distribution
        print("Experience Level Distribution:")
        calculate_stat.get_experience_level_distribution(filteredData).show()
        print()

        # Print salary statistics by experience level
        print("Salary Statistics by Experience Level:")
        calculate_stat.calculate_salary_stats_by_experience(filteredData).show()
        print()

        # Print high paying jobs analysis using Spark SQL
        print("High Paying Jobs Analysis (SQL):")
        calculate_stat.analyze_high_paying_jobs_sql(filteredData).show(truncate=False)
        print()

        # Print salary distribution analysis using PySpark
        print(
            """
        Process:
        1. Categorizes salaries into 4 ranges (Entry/Mid/Senior/Executive Level)
        2. Groups data by experience level and salary range
        3. Calculates count, average salary, standard deviation, and percentage for each group
        """
        )
        print(
            "Salary Distribution Analysis by Experience Level and Salary Range (data transformation):"
        )
        calculate_stat.analyze_salary_trends(filteredData).show(truncate=False)
        print()

    finally:
        # Stop Spark session
        spark.stop()


if __name__ == "__main__":
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        main()
    output = captured_output.getvalue()

    generate_markdown.generate_markdown(output)
