from pystock_hts import Daishin

stock_code_list = ["A005930", "A252670", "A114800", "A251340", "A122630", "A233740"] #삼성전자, KODEX 200선물인버스 2X, KODEX 인버스, KODEX 코스닥 150선물인버스, KODEX 레버리지, KODEX 코스닥150 레버리지


for stock_code in stock_code_list:
  res = Daishin.CpSysDib().getStockChartPriceToDate(60, stock_code)
  print(res)