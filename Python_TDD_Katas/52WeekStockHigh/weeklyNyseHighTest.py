# Weekly NYSE 52 High Weekly API TDD Experiment
import unittest
import json
from weeklyNyseHigh import StockDaily52
from datetime import date, timedelta
import datetime

class TestStockHighNyse(unittest.TestCase):
    def setUp(self):
        self.testApiHighsEx1 = json.dumps([
                                {'20150924': {
									"AGOG": {
                                        "name": 'Assured Guaranty Municipal Holding 6.25% Notes 2102',
                                        "52weekHigh": 25.6, 
										"price": 25.57, 
										'changeAmount': .07, 
										'changePrecent': .27, 
										'volume': 23447, 
										'webGraph': 'http://quotes.wsj.com/AGOG'
									},
									"CUBE": {
                                        'name': 'CubeSmart',
										"52weekHigh": 26.94, 
										"price": 26.54, 
										'changeAmount': -.23, 
										'changePrecent': -.86, 
										'volume': 2234212, 
										'webGraph': 'http://quotes.wsj.com/CUBE'
									},
									"AKOB": {
                                        'name': 'Embotelladora Andina S.A. (Series B) ADR',
										"52weekHigh": 23.74, 
										"price": 23.65, 
										'changeAmount': .48, 
										'changePrecent': 2.07, 
										'volume': 41559, 
										'webGraph': 'http://quotes.wsj.com/AKOB'
									}, 
									"AKOA": {
                                        'name': 'Embotelladora Andina S.A. (Series A) ADR',
										"52weekHigh": 18.68, 
										"price": 18.68, 
										'changeAmount': .48, 
										'changePrecent': 2.64, 
										'volume': 2385, 
										'webGraph': 'http://quotes.wsj.com/AKOA'
									}, 
									"FNBE": {
                                        'name': 'F.N.B. Dep. pfd. (Rep. 1/40th Interest Fixed-to-Floating Rate Non-Cum. Perp. pfd. Series E)',  
										"52weekHigh":29.75, 
										"price": 29.75, 
										'changeAmount': .95, 
										'changePrecent': 3.3, 
										'volume': 3735, 
										'webGraph': 'http://quotes.wsj.com/FNBE'
									},
									"FBC": {
                                        'name': 'Flagstar Bancorp',
										"52weekHigh": 21.01, 
										"price": 21.01, 
										'changeAmount': .3, 
										'changePrecent': 1.45, 
										'volume': 149343, 
										'webGraph': 'http://quotes.wsj.com/FBC'
									},
									"FLO": {
                                        'name':'Flowers Foods',
										"52weekHigh": 25.5, 
										"price": 25.40, 
										'changeAmount': .09, 
										'changePrecent': .36, 
										'volume': 1473637, 
										'webGraph': 'http://quotes.wsj.com/FLO'
									}
								}	
                            }])
        self.testApiHighsEx2 = json.dumps([
                                {'20150922': {
									"AFST": {
                                        "name": "AmTrust Financial Services 7.5% Sub. Notes 111555", 
										"52weekHigh": 25.09, 
										"price": 25.03, 
										'changeAmount': .09, 
										'changePrecent': .36, 
										'volume': 134392, 
										'webGraph': 'http://quotes.wsj.com/AFST'
									}, 
									"CNXC": {
                                        "name": "CNX Coal Resources",
										"52weekHigh": 17.34, 
										"price": 14.35, 
										'changeAmount': -.07, 
										'changePrecent': -.49, 
										'volume': 53575, 
										'webGraph': 'http://quotes.wsj.com/CNXC'
									}, 
									"CVC": {
                                        "name": "Cablevision Systems",
										"52weekHigh": 33.27, 
										"price": 33.05, 
										'changeAmount': -.07, 
										'changePrecent': -.21, 
										'volume': 7161291, 
										'webGraph': 'http://quotes.wsj.com/CVC'
									}, 
									"FLO": {
                                        "name": "Flowers Foods",
										"52weekHigh": 24.82, 
										"price": 24.74, 
										'changeAmount': .38, 
										'changePrecent': 1.56, 
										'volume': 1686420, 
										'webGraph': 'http://quotes.wsj.com/FLO'
									} 
								}	
							}])
        self.testApiHighsEx3 = json.dumps([
                                {'20150928': {
									"AIY": {
                                        "name": "Apollo Investment 6.875% Sr. Notes due 2043", 
										"52weekHigh": 26.13, 
										"price":  25.87,
										'changeAmount': -0.02, 
										'changePrecent': -0.06, 
										'volume': 4012, 
										'webGraph': 'http://quotes.wsj.com/AIY'
									}, 
									"CVT": {
                                        "name": "Cvent",
										"52weekHigh": 34.27, 
										"price": 33.80, 
										'changeAmount': 0.57, 
										'changePrecent': 1.72 , 
										'volume': 484462, 
										'webGraph': 'http://quotes.wsj.com/CVT'
									}, 
									"FNFV": {
                                        "name": "Fidelity National Financial Tracking Stock Wi",
										"52weekHigh": 11.71, 
										"price": 11.00, 
										'changeAmount': -0.61 , 
										'changePrecent': -5.25, 
										'volume': 3871, 
										'webGraph': 'http://quotes.wsj.com/FNFV'
									}, 
									"FLO": {
                                        "name": "Flowers Foods",
										"52weekHigh": 25.93, 
										"price": 25.24, 
										'changeAmount': -0.16, 
										'changePrecent': -0.63 , 
										'volume': 1824359 , 
										'webGraph': 'http://quotes.wsj.com/FLO'
									}, 
									"NEEQ": {
                                        "name": "NextEra Energy Un",
										"52weekHigh": 53.26, 
										"price": 51.31, 
										'changeAmount': -0.56, 
										'changePrecent': -1.08, 
										'volume': 294622 , 
										'webGraph': 'http://quotes.wsj.com/NEEQ'
									} 
								}	
							}])
    
    def test_date_Sep24_2015_Json_of_dayHighStocks_whichInclude_stockName_52weekHighPrice_currentPrice_changeForTheDay_percentChangeForDay_volume(self):
		stock = StockDaily52('2015', '09', '24')
		self.assertEqual(self.testApiHighsEx1 , stock.stockHighs())

    def test_date_Sep22_2015_Json_of_dayHighStocks_whichInclude_stockName_52weekHighPrice_currentPrice_changeForTheDay_percentChangeForDay_volume(self):
		stock = StockDaily52('2015', '09', '22')
		self.assertEqual(self.testApiHighsEx2 , stock.stockHighs())

    def test_date_Sep28_2015_Json_of_dayHighStocks_whichInclude_stockName_52weekHighPrice_currentPrice_changeForTheDay_percentChangeForDay_volume(self):
		stock = StockDaily52('2015', '09', '28')
		self.assertEqual(self.testApiHighsEx3 , stock.stockHighs())

    def test_date_Sep26_2015_Json_of_dayHighStocks_whichInclude_stockName_52weekHighPrice_currentPrice_changeForTheDay_percentChangeForDay_volume(self):
        with self.assertRaises( Exception) as context: 
            StockDaily52('2015', '09', '26')
        self.assertIn("this is not weekday", context.exception.message)

    def test_enterting_string_thats_not_nums_should_raise_exception(self):
        with self.assertRaises(Exception) as context:
            StockDaily52('5', '8', 'my')
        self.assertIn("invalid entry", context.exception.message)

        with self.assertRaises(Exception) as context:
            StockDaily52('my', '8', '9')
        self.assertIn("invalid entry", context.exception.message)

        with self.assertRaises(Exception) as context:
            StockDaily52('my', '8', 'my')
        self.assertIn("invalid entry", context.exception.message)

    def test_can_only_request_52_info_up_untill_may_1_2007(self):
        with self.assertRaises(Exception) as context:
            StockDaily52('2007', '4', '30')
        self.assertIn("No data prior to 2007 May 1st", context.exception.message)

    def test_can_only_request_days_after_today(self):
        with self.assertRaises(Exception) as context:
            tomorrow = datetime.date.today() + timedelta(days=1)
            StockDaily52(str(tomorrow.year),\
                str(tomorrow.month), str(tomorrow.day))
        self.assertIn("No information for future dates",context.exception.message) 

if __name__ == '__main__':
    unittest.main()


