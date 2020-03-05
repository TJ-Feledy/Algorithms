#!/usr/bin/python
"""
- receives a list
- return max profit
- must buy before sell (number to sell must be after number to buy, in the list)
for each price in the list:
  -find the difference between it and each price before it
  -check if current difference is > the last diff.:
    -if its greater, save it in a variable
return the biggest profit.
"""
import argparse

def find_max_profit(prices):
  max_profit = 0
  index = 0
  for i in range(0, len(prices)):
    for i2 in range(0, index):
      if i2 == index:
        index += 1
        print(i)
      else:
        while i2 < index:
          print(max_profit)
          diff = prices[index] - prices[i2]
          
          if diff > max_profit:
            max_profit = diff
            return max_profit
          
          index += 1
  
  return max_profit


find_max_profit([20, 60,200,40,10])

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))