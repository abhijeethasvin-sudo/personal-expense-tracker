"""Small tests for the expense tracker. Run with python3 -m unittest discover -s tests -v."""

import tempfile
import unittest
from pathlib import Path

from main import calculate_total, category_totals, load_expenses, save_expenses


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.expenses = [
            {"description": "Coffee", "amount": 4.50, "category": "Food"},
            {"description": "Bus", "amount": 3.25, "category": "Travel"},
            {"description": "Lunch", "amount": 12.00, "category": "food"},
        ]

    def test_empty_total(self):
        self.assertEqual(calculate_total([]), 0)

    def test_total(self):
        self.assertAlmostEqual(calculate_total(self.expenses), 19.75)

    def test_category_totals(self):
        totals = category_totals(self.expenses)
        self.assertAlmostEqual(totals["Food"], 16.50)
        self.assertAlmostEqual(totals["Travel"], 3.25)

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            file_name = Path(folder) / "test_expenses.csv"
            save_expenses(self.expenses, file_name)
            self.assertEqual(load_expenses(file_name), self.expenses)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_expenses(Path(folder) / "missing.csv"), [])


if __name__ == "__main__":
    unittest.main()
