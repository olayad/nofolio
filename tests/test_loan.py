#!/usr/bin/env python3

import unittest
import sys
import os
sys.path.append(os.path.realpath('.'))
# sys.path.append('../')
# print(sys.path)
import loan
import exceptions
import tools
import datetime

class TestLoan(unittest.TestCase):

    # def test_invalid_loan_csv_data(self):
    #     loan.set_test_mode('throws_invalid_loan_data.csv')
    #     self.assertRaises(exceptions.InvalidLoanData, loan.init_loans)
    #
    #
    # def test_single_loan_no_collateral_updates(self):
    #     loan.set_test_mode('loans_1.csv')
    #     loan.init_loans()
    #     self.assertEqual(len(loan.Loan.active_loans), 1, 'Should be 1 loan')
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 1,
    #                      "Should be 1 entry in collateral history")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 1.0,
    #                      'Should be 1.0 in total collateral')
    #
    # def test_single_loan_multiple_collateral_increases(self):
    #     loan.set_test_mode('loans_2.csv')
    #     loan.init_loans()
    #     df_stats = loan.Loan.active_loans[0].stats
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 3,
    #                      "Should be 3")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 6.0,
    #                      'Should be 6.0 in current collateral')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      1.0, 'Should be 1.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-10']['collateral_amount'].values[0],
    #                      3.0, 'Should be 3.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-20']['collateral_amount'].values[0],
    #                      6.0, 'Should be 6.0 in collateral_amount')
    #
    # def test_multiple_loans_multiple_collateral_increases(self):
    #     loan.set_test_mode('loans_3.csv')
    #     loan.init_loans()
    #     self.assertEqual(len(loan.Loan.active_loans), 2, "Should be 2")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 3.0,
    #                      'Should be 3.0 in current collateral')
    #     self.assertEqual(loan.Loan.active_loans[1].current_collateral, 10.0,
    #                      'Should be 10.0 in current collateral')
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 2, "Should be 2")
    #     self.assertEqual(len(loan.Loan.active_loans[1].collateral_history), 4, "Should be 4")
    #     df_stats0 = loan.Loan.active_loans[0].stats
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-10-01']['collateral_amount'].values[0],
    #                      1.0, 'Should be 1.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-10-15']['collateral_amount'].values[0],
    #                      3.0, 'Should be 3.0 in collateral_amount')
    #     df_stats1 = loan.Loan.active_loans[1].stats
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      1.0, 'Should be 1.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-12']['collateral_amount'].values[0],
    #                      3.0, 'Should be 3.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-13']['collateral_amount'].values[0],
    #                      6.0, 'Should be 6.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-15']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #
    # def test_single_loan_multiple_collateral_decreases(self):
    #     loan.set_test_mode('loans_4.csv')
    #     loan.init_loans()
    #     df_stats = loan.Loan.active_loans[0].stats
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 3,
    #                      "Should be 3")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 5.0,
    #                      'Should be 5.0 in current collateral')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-10']['collateral_amount'].values[0],
    #                      8.0, 'Should be 3.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-20']['collateral_amount'].values[0],
    #                      5.0, 'Should be 5.0 in collateral_amount')
    #
    #
    # def test_single_loan_multiple_collateral_increases_and_decreases(self):
    #     loan.set_test_mode('loans_5.csv')
    #     loan.init_loans()
    #     df_stats = loan.Loan.active_loans[0].stats
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 5,
    #                      "Should be 5")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 4.0,
    #                      'Should be 4.0 in current collateral')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      8.0, 'Should be 8.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-10']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-20']['collateral_amount'].values[0],
    #                      9.0, 'Should be 9.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-21']['collateral_amount'].values[0],
    #                      7.0, 'Should be 7.0 in collateral_amount')
    #     self.assertEqual(df_stats[df_stats['date'] == '2019-11-22']['collateral_amount'].values[0],
    #                      4.0, 'Should be 4.0 in collateral_amount')
    #
    #
    # def test_multiple_loans_multiple_cad_borrowed_increases(self):
    #     loan.set_test_mode('loans_6.csv')
    #     loan.init_loans()
    #     self.assertEqual(loan.Loan.active_loans[0].current_borrowed_cad, 10000,
    #                      'Should be 10000 in current cad borrowed')
    #     self.assertEqual(loan.Loan.active_loans[1].current_borrowed_cad, 6000,
    #                      'Should be 6000 in current cad borrowed')
    #     self.assertEqual(len(loan.Loan.active_loans[0].borrowed_cad_history), 4, "Should be 4 updates")
    #     self.assertEqual(len(loan.Loan.active_loans[1].borrowed_cad_history), 3, "Should be 3 updates")
    #     df_stats0 = loan.Loan.active_loans[0].stats
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-01']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-04']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-05']['borrowed_cad'].values[0],
    #                      3000, 'Should be 3000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-09']['borrowed_cad'].values[0],
    #                      3000, 'Should be 3000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-10']['borrowed_cad'].values[0],
    #                      6000, 'Should be 6000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-19']['borrowed_cad'].values[0],
    #                      6000, 'Should be 6000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-20']['borrowed_cad'].values[0],
    #                      10000, 'Should be 10000 in borrowed_cad')
    #     df_stats1 = loan.Loan.active_loans[1].stats
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-01']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-10']['borrowed_cad'].values[0],
    #                      3000, 'Should be 3000 in borrowed_cad')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-20']['borrowed_cad'].values[0],
    #                      6000, 'Should be 60000 in borrowed_cad')
    #
    # def test_multiple_loans_multiple_updates_in_collateral_and_cad_borrowed(self):
    #     loan.set_test_mode('loans_7.csv')
    #     loan.init_loans()
    #     self.assertEqual(len(loan.Loan.active_loans), 2, "Should be 2 active loans")
    #     self.assertEqual(loan.Loan.active_loans[0].current_collateral, 4.0,
    #                      'Should be 4.0 in current collateral')
    #     self.assertEqual(loan.Loan.active_loans[1].current_collateral, 10.0,
    #                      'Should be 10.0 in current collateral')
    #     self.assertEqual(loan.Loan.active_loans[0].current_borrowed_cad, 3000,
    #                      'Should be 3000 in current cad borrowed')
    #     self.assertEqual(loan.Loan.active_loans[1].current_borrowed_cad, 6000,
    #                      'Should be 6000 in current cad borrowed')
    #
    #     self.assertEqual(len(loan.Loan.active_loans[0].collateral_history), 4, "Should be 4 updates")
    #     self.assertEqual(len(loan.Loan.active_loans[1].collateral_history), 3, "Should be 3 updates")
    #     df_stats0 = loan.Loan.active_loans[0].stats
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-04']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-05']['collateral_amount'].values[0],
    #                      7.0, 'Should be 7.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-06']['collateral_amount'].values[0],
    #                      7.0, 'Should be 7.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-10']['collateral_amount'].values[0],
    #                      8.0, 'Should be 8.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-11']['collateral_amount'].values[0],
    #                      8.0, 'Should be 8.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-21']['collateral_amount'].values[0],
    #                      4.0, 'Should be 4.0 in collateral_amount')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-22']['collateral_amount'].values[0],
    #                      4.0, 'Should be 4.0 in collateral_amount')
    #
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-01']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-21']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-22']['borrowed_cad'].values[0],
    #                      3000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-23']['borrowed_cad'].values[0],
    #                      3000, 'Should be 1000 in borrowed_cad')
    #
    #     df_stats1 = loan.Loan.active_loans[1].stats
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-01']['collateral_amount'].values[0],
    #                      10.0, 'Should be 1.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-09']['collateral_amount'].values[0],
    #                      10.0, 'Should be 1.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-10']['collateral_amount'].values[0],
    #                      5.0, 'Should be 5.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-11']['collateral_amount'].values[0],
    #                      5.0, 'Should be 5.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-20']['collateral_amount'].values[0],
    #                      10.0, 'Should be 6.0 in collateral_amount')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-21']['collateral_amount'].values[0],
    #                      10.0, 'Should be 10.0 in collateral_amount')
    #
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-01']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-19']['borrowed_cad'].values[0],
    #                      1000, 'Should be 1000 in borrowed_cad')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-20']['borrowed_cad'].values[0],
    #                      6000, 'Should be 60000 in borrowed_cad')
    #     self.assertEqual(df_stats1[df_stats1['date'] == '2019-11-21']['borrowed_cad'].values[0],
    #                      6000, 'Should be 60000 in borrowed_cad')
    #
    # def test_collateralization_ratio(self):
    #     loan.set_test_mode('loans_8.csv')
    #     loan.init_loans()
    #     df_stats0 = loan.Loan.active_loans[0].stats
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-01']['collateralization_ratio'].values[0],
    #                      2.05, 'Should be 2.05 in collateralization_ratio')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-02']['collateralization_ratio'].values[0],
    #                      3.09, 'Should be 3.09 in collateralization_ratio')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-03']['collateralization_ratio'].values[0],
    #                      2.55, 'Should be 2.55 in collateralization_ratio')
    #     self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-04']['collateralization_ratio'].values[0],
    #                      2.41, 'Should be 2.41 in collateralization_ratio')

    def test_updating_ratio_with_current_price(self):
        loan.set_test_mode('loans_9.csv')
        loan.init_loans()
        df_stats0 = loan.Loan.active_loans[0].stats
        self.assertEqual(df_stats0[df_stats0['date'] == '2019-11-01']['collateralization_ratio'].values[0],
                         2.05, 'Should be 2.05 in collateralization_ratio')
        loan.update_ratios_with_current_price(price_given=123456.0)
        date_to_update = tools.get_current_date_for_exchange_api()
        self.assertEqual(df_stats0[df_stats0['date'] == date_to_update]['usd_price'].values[0],
                         123456.0, 'Should be 123456.0 in usd_price')
        cad_price = df_stats0.loc[df_stats0['date'] == date_to_update, 'cad_price'].values[0]
        collateral_amount = df_stats0.loc[df_stats0['date'] == date_to_update, 'collateral_amount'].values[0]
        borrowed_cad = df_stats0.loc[df_stats0['date'] == date_to_update, 'borrowed_cad'].values[0]
        new_ratio = round((cad_price * collateral_amount) / borrowed_cad, 2)
        self.assertEqual(df_stats0[df_stats0['date'] == date_to_update]['collateralization_ratio'].values[0],
                         new_ratio, 'Should be new collateralization_ratio')

    # def test_here(self):
    #     # print(tools.get_usd_price())
    #     loan.set_test_mode('loans_8.csv')
    #     loan.init_loans()
    #     df_stats0 = loan.Loan.active_loans[0].stats
    #     print(df_stats0)
    #     print()
    #     print()
    #     # print('today fx rate:', tools.get_fx_cadusd_rates(start_date='2019-12-03', end_date='2019-12-03'))
    #     # tools.get_current_date_for_exchange_api()
    #     loan.update_ratios_with_current_price(price_given=99999)
    #     print(df_stats0)
    #     # for x in loan.Loan.active_loans:
    #     #     x.update_stats_entry('2019-12-02', 99999)

if __name__ == '__main__':
    unittest.main()

