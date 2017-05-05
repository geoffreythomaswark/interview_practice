import random

def get_max_profit(stock_prices_yesterday):

    # ensure there are at least 2 prices given
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Cannot get profit!  Need at least 2 historical prices.')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip 1st time
        if index == 0:
            continue

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit

# randomize historical stock prices
stock_prices_yesterday = random.sample(range(0,50), 10)

#NEGTESTstock_prices_yesterday = [25, 20, 14, 10, 1] -> -4
#OLDTESTstock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print stock_prices_yesterday
print get_max_profit(stock_prices_yesterday)
#OLDTEST returns 6 (buying for $5 and selling for $11)
