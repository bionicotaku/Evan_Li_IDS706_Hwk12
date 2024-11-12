import unittest
import io
from contextlib import redirect_stdout
import os
from main import main
from pyspark.sql import SparkSession


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a Spark session for the test class
        cls.spark = SparkSession.builder.appName("TestSalaryAnalysis").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        # Stop Spark session after all tests
        if cls.spark is not None:
            cls.spark.stop()

    def test_main(self):
        # Check if the dataset file exists
        dataset_path = "data/Dataset-salary-2024.csv"
        self.assertTrue(
            os.path.exists(dataset_path), f"Dataset file {dataset_path} does not exist."
        )

        # Capture and test output
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main()
        output = captured_output.getvalue()

        # Verify all expected sections are present in the output
        expected_sections = [
            "Salary Statistics:",
            "Top 20 Job Titles Distribution:",
            "Experience Level Distribution:",
            "Salary Statistics by Experience Level:",
            "High Paying Jobs Analysis (SQL):",
            "Salary Distribution Analysis by Experience Level and Salary Range",
        ]

        for section in expected_sections:
            self.assertIn(section, output)

        # Check if the markdown file was generated
        markdown_file = "analysis_results.md"
        self.assertTrue(
            os.path.exists(markdown_file),
            f"Markdown file {markdown_file} was not generated.",
        )


if __name__ == "__main__":
    unittest.main()
