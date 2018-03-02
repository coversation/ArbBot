import requests
import time


while True:
	nakedBuyUrlTO = "https://tradeogre.com/api/v1/order/buy?market=BTC-LTC&quantity=&price="
	nakedBuyUrlTS = "https://tradesatoshi.com/api/private/submitorder?market=LTC_BTC&type=buy&amount=&price="
	#Set up TradeSatoshi API request
	orderBookTS = requests.get('https://tradesatoshi.com/api/public/getorderbook?market=LTC_BTC&type=both&depth=20')
	orderDataTS = orderBookTS.json()
	orderBookBuyQtyTS = float(orderDataTS["result"]["buy"][0]["quantity"]) #Quantity of the highest price buy order on TS
	orderBookBuyPriceTS = float(orderDataTS["result"]["buy"][0]["rate"]) #Price of the highest price buy order on TS
	orderBookSellQtyTS = float(orderDataTS["result"]["sell"][0]["quantity"]) #Quantity of the lowest price sell order on TS
	orderBookSellPriceTS = float(orderDataTS["result"]["sell"][0]["rate"]) #Price of the lowest price sell order on TS

	#Set up TradeOgre API request
	orderBookTO = requests.get('https://tradeogre.com/api/v1/orders/BTC-LTC')
	orderDataTO = orderBookTO.json()
	tempOrderBookBuyPriceTO = sorted(orderDataTO["buy"].keys()) #Price of the highest price buy order on TO
	tempOrderBookBuyPriceTO.reverse()
	orderBookBuyPriceTO = float(tempOrderBookBuyPriceTO[0])
	orderBookBuyQtyTO = orderDataTO["buy"][tempOrderBookBuyPriceTO[0]] #Quantity of the highest price buy order on TO
	tempOrderBookSellPriceTO = sorted(orderDataTO["sell"].keys()) #Price of the lowest price sell order on TO
	orderBookSellPriceTO = float(tempOrderBookSellPriceTO[0])
	orderBookSellQtyTO = orderDataTO["sell"][tempOrderBookSellPriceTO[0]] #Quantity of the lowest price sell order on TO

	print(str(orderBookBuyQtyTO) + " for buy at " + str(orderBookBuyPriceTO) + " on TO")
	print("")
	print(str(orderBookSellQtyTO) + " for sale at " + str(orderBookSellPriceTO) + " on TO")
	print("")
	print(str(orderBookBuyQtyTS) + " for buy at " + str(orderBookBuyPriceTS) + " on TS")
	print("")
	print(str(orderBookSellQtyTS) + " for sale at " + str(orderBookSellPriceTS) + " on TS")
	print("")

	if orderBookBuyPriceTS > orderBookBuyPriceTO: #If buy is higher on TS
		print("LTC buying for higher at TS")
		if orderBookSellPriceTO < orderBookBuyPriceTS: #AND if sell is lower on TO
			print("arbitrage opportunity, buy on TO sell on TS")
			if (orderBookBuyQtyTS*0.998) > orderBookSellQtyTO:
				print("Buy out TO, sell that much on TS")
				buyUrlTO = nakedBuyUrlTO[:70] + str(orderBookSellPriceTO)
				buyUrlTO = buyUrlTO[:63] + str(orderBookSellQtyTO) + buyUrlTO[63:]
				print(buyUrlTO)
			else:
				print("Buy equal to TS QTY on TO, sell that much on TS")
				buyUrlTO = nakedBuyUrlTO[:70] + str(orderBookSellPriceTO)
				buyUrlTO = buyUrlTO[:63] + str(orderBookBuyQtyTS) + buyUrlTO[63:]
				print(buyUrlTO)

	if (orderBookBuyPriceTO*0.998) > orderBookBuyPriceTS: #If buy is higher on TO
		print("LTC buying for higher at TO")
		if orderBookBuyPriceTS < orderBookSellPriceTO: #AND if sell is lower on TS
			print("arbitrage opportunity, buy on TS sell on TO")
			if (orderbookBuyQtyTS*0.998) > orderBookSellQtyTO:
				print("Buy equal to TO QTY on TS, sell that much on TO")
				buyUrlTS = nakedBuyUrlTS[:87] + str(orderBookSellPriceTS)
				buyUrlTS = buyUrlTS[:80] + str(orderBookBuyQtyTS) + buyUrlTS[80:]
				print(buyUrlTS)
			else:
				print("Buy out TS, sell that much on TO")
				buyUrlTS = nakedBuyUrlTS[:87] + str(orderBookSellPriceTS)
				buyUrlTS = buyUrlTS[:80] + str(orderBookSellQtyTS) + buyUrlTS[80:]
				print(buyUrlTS)

	print("")
	print(time.asctime( time.localtime(time.time()) ))
	time.sleep(20)