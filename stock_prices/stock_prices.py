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
  for i in range(index, len(prices)):
    while i < index:
      diff = 0
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))