from pystock_hts import Daishin

daishin_sys = Daishin.CpSysDib()
daishin_util = Daishin.CpUtil()
daishin_trade = Daishin.CpTrade()

is_connected = daishin_util.getConnected()
print(f"is_connected: {is_connected}")

stock_name = daishin_util.getStockCodeToName("A005930")
print(f"stock_name: {stock_name}")

stock_price = daishin_sys.getStockChartPriceToDate(2, "A005930")
print(f"stock_price: {stock_price}")

stock_per = daishin_sys.getStockPer("A005930")
print(f"stock_per: {stock_per}")

is_buyed = daishin_trade.buyStock("A005930")
print(f"is_buyed: {is_buyed}")

is_selled = daishin_trade.sellStock("A005930")
print(f"is_selled: {is_selled}")
      