stocks = {"AAPL": 110, "GOOG": 230, "TSLA": 400, "AMZN": 3000}
price_threshold = 200

print("We know about these stock prices.")
print(stocks)

print("These stocks are over our threshold of", price_threshold)

for stock, price in stocks.items():
    if price > price_threshold:
        print(stock, ":", price)
