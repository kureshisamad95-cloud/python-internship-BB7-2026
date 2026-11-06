prices = [100,200,300,400,500,600,700,800,900,1000]

average_price = sum(prices) / len(prices)

above_average = [price for price in prices if price > average_price]

print("Product prices:", prices)

print("Average prices:",average_price)

print("Prices above average:", above_average)
