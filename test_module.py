import unittest
import demographic_data_analyzer

class DemographicAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.results = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        self.assertTrue('race_count' in self.results)

    def test_average_age_men(self):
        self.assertIsInstance(self.results['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertGreaterEqual(self.results['percentage_bachelors'], 0)

    def test_higher_education_rich(self):
        self.assertGreaterEqual(self.results['higher_education_rich'], 0)

    def test_lower_education_rich(self):
        self.assertGreaterEqual(self.results['lower_education_rich'], 0)

    def test_min_work_hours(self):
        self.assertGreater(self.results['min_work_hours'], 0)

    def test_rich_percentage(self):
        self.assertGreaterEqual(self.results['rich_percentage'], 0)

    def test_highest_earning_country(self):
        self.assertIsInstance(self.results['highest_earning_country'], str)

    def test_highest_earning_country_percentage(self):
        self.assertGreaterEqual(self.results['highest_earning_country_percentage'], 0)

    def test_top_IN_occupation(self):
        self.assertIsInstance(self.results['top_IN_occupation'], str)

if __name__ == "__main__":
    unittest.main()
