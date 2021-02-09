from ast import Num
from pystock_hts import Daishin
import time

def getKValue(high_price_list, low_price_list, last_price_list, start_price_list):
  high_price_all = 0
  low_price_all = 0
  last_price_all = 0
  start_price_all = 0
  i = 0
  for high_price, low_price, last_price, start_price in zip(high_price_list, low_price_list, last_price_list, start_price_list):
    high_price_all += Num(high_price)
    low_price_all += Num(low_price)
    last_price_all += Num(last_price)
    start_price_all += Num(start_price)
    i += 1
    if i > 20:
      i -= 1
    high_price_all -= Num(high_price)
    low_price_all -= Num(low_price)
    last_price_all -= Num(last_price)
    start_price_all -= Num(start_price)

  return 1-abs((start_price_all - last_price_all)/(high_price_all - low_price_all))
      

k = 0.5
all_revenue_of_k = 0

stock_list = ["A005930", "A114800", "A069500", "A229200", "A251340"] #삼성전자, KODEX 인버스, KODEX 200, KODEX 코스닥 150, KODEX 코스닥150선물인버스

for stock_code in stock_list:
  print("wait")
  time.sleep(3)
  print("wait done")
  
  date_list, stock_start_price_list, stock_high_price_list, stock_low_price_list, stock_last_price_list = Daishin.CpSysDib().getStockChartPriceToDate(21, stock_code)
  
  del date_list[0]
  del stock_start_price_list[0]
  del stock_high_price_list[0]
  del stock_low_price_list[0]
  del stock_last_price_list[0]

  k = getKValue(date_list, stock_low_price_list, stock_last_price_list, stock_start_price_list)

  average = None
  before_last_price = 0
  win = 0
  lose = 0
  revenue = 0

  for date, high_price, low_price, last_price in zip(date_list, stock_high_price_list, stock_low_price_list, stock_last_price_list):
    print(date, high_price, low_price, last_price)
    if not average:
      average = int((high_price - low_price) * k)
      before_last_price = last_price
      continue
    
    goal_price = before_last_price + average
    
    if goal_price >= high_price:
      before_last_price = last_price
      continue
      
    if goal_price < last_price:
      win += 1
    else:
      lose += 1
      
    revenue = revenue + last_price - goal_price
    before_last_price = last_price
    
  print(Daishin.CpUtil().getStockCodeToName(stock_code))
  print(stock_code)
  print("revenue: ", revenue)
  print("win: ", win)
  print("lose: ", lose)
  all_revenue_of_k += revenue

print(f"{k}", all_revenue_of_k)
print()
print()
