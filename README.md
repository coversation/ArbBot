# ArbBot
The bot checks the buy price&quantity and sell price&quantity on each exchange. Currently only looks at TradeSatoshi and TradeOgre.
Currently written to look at Litecoin, BTC-LTC pairing.

It checks a few scenarios. An example:

If the buy price is higher on TradeSatoshi than the sell price on TradeOgre, there is an arbitrage opportunity to buy on TradeOgre and sell on TradeSatoshi.
The bot then checks the quantities to figure out how much to buy/sell.
If the buy quantity on TradeSatoshi is greater than the sell quantity on TradeOgre:
	The bot would buy all of the available stock on TradeOgre for whatever price, then sell that much on TradeSatoshi.
If the buy quantity on TradeSatoshi is less than the sell quantity on Tradeogre:
	The bot would buy an amount on TradeOgre equal to the buy quantity on TradeSatoshi, then sell that much on Tradesatoshi.

Currently the price checks seem to work just fine and the simple logic determining when trades would occur also seems to work.
My price check API calls are really messy, it seems to get the correct values but I'm positive it could be better/simpler.

I also have not implemented the sell API calls. And the private API URLs don't include any keys.
