#!/usr/bin/env python3

import unittest
import sys
import os
sys.path.append('../src')
# from datetime import datetime, timedelta
import pandas as pd
import config as cfg
import savings
# import loan
import exceptions
# import tools
# from debt import Debt


class TestSavings(unittest.TestCase):
    def setUp(self):
        pass
        # Show all rows/columns when pandas DF is printed
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

    def test_invalid_csv_file(self):
        cfg.set_test_mode('savings_does_not_exist.csv')
        self.assertRaises(exceptions.InitializationDataNotFound, savings.init_savings)

    def test_total_savings_btc(self):
        cfg.set_test_mode('savings_0.csv')
        self.assertEqual(savings.get_total_btc(), 0, 'Should be 0')

if __name__ == '__main__':
    unittest.main()

