# Scraping 52 week Stock High Kata

##Background
This kata allows one to enter a date and that date brings up the stock: 
* Symbol, 52 week high, current price, amout stock has changed since yesterday, the precent the stock has changed since yesterday, the volume of the stock, and a web site which diplays a graph of stock info

### 52 week high
* cant grab data from before may 1st 2007(may change not 100% sure)
* cant grab data past current today because it has not been determined
* should return symbol, name, 52 week high, price, change (amount and %) and stock Volume
* cant request information for day that is a weekend

### Feature:
* if you want to know the stock 52 week highs for any day from today to may 1st 2007 just enter year, month day as a string and then call function stockHighs()

* This is a portion of a larger system

### potential errors:
* doesnt catch days that the market is closed (holidays)

