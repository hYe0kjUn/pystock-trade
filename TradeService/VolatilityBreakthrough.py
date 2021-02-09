from pystock_hts import Daishin

def getKValue(high_price_list, low_price_list, last_price_list, start_price_list):
  high_price_all = 0
  low_price_all = 0
  last_price_all = 0
  start_price_all = 0
  i = 0
  for high_price, low_price, last_price, start_price in zip(high_price_list, low_price_list, last_price_list, start_price_list):
    high_price_all += high_price
    low_price_all += low_price
    last_price_all += last_price
    start_price_all += start_price
    i += 1
    if i > 20:
      i -= 1
    high_price_all -= high_price
    low_price_all -= low_price
    last_price_all -= last_price
    start_price_all -= start_price

  return 1-abs((start_price_all - last_price_all)/(high_price_all - low_price_all))

def VolatilityBreakthroughBuyBot():
  last_start_price = 0
  last_last_price = 0
  last_high_price = 0
  last_low_price = 0
  k = 0.5
  
  
  
  
def VolatilityBreakthroughSellBot():
  return

date_list, start_price_list, high_price_list, low_price_list, last_price_list = Daishin.CpSysDib().getStockChartPriceToDate(21, "A229200")
print(date_list, start_price_list, high_price_list, low_price_list, last_price_list)
print(getKValue(high_price_list, low_price_list, last_price_list, start_price_list))