from pystock_hts import Daishin
import time

k = 0.5
ratelimit = 0
all_revenue_of_k = 0

stock_list = ["A005930", "A252670", "A114800", "A251340", "A122630", "A233740"] #삼성전자, KODEX 200선물인버스 2X, KODEX 인버스, KODEX 코스닥 150선물인버스, KODEX 레버리지, KODEX 코스닥150 레버리지

for stock_code in stock_list:
  
  date_list, stock_high_price_list, stock_low_price_list, stock_last_price_list = Daishin.CpSysDib().getStockChartPriceToDate(30, stock_code)
  ratelimit += 4
  
  average = None
  before_last_price = 0
  win = 0
  lose = 0
  revenue = 0

  for date, high_price, low_price, last_price in zip(date_list, stock_high_price_list, stock_low_price_list, stock_last_price_list):
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
    
  print(stock_code)
  print("revenue: ", revenue)
  print("win: ", win)
  print("lose: ", lose)
  all_revenue_of_k += revenue
  print("wait")
  time.sleep(15)
  
print(f"{k}", all_revenue_of_k)
print()
print()
