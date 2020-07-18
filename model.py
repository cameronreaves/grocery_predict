import pandas as pd
import math
import sys


data = pd.read_csv("data/shopping.csv")
data.dropna(inplace=True)

def get_list(filename):
    items = dict()

    with open(filename) as file:
        for line in file:
            l = line.split()
            items[l[1].lower().title()] = int(l[0])
    return items

def estimate(items):
    est = 0
    count = 0
    message = []

    for item, number in items.items():
        avg = data[data.loc[:,"Item"].str.contains(item)].loc[:,'Per'].mean()
        if not math.isnan(avg):
            est += avg * number
        else:
            count += 1
            message.append(item)
    return [count, message, est]

if __name__ == "__main__":

    items = get_list(sys.argv[1])
    output = estimate(items)
    print('There are {} missing items in your list : {} \n Estimate cost = {}'.format(output[0], output[1], output[2]))