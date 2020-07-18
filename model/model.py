import math

def get_list(filename):
    items = dict()

    with open(filename) as file:
        for line in file:
            l = line.split()
            items[l[1].lower().title()] = int(l[0])
    return items

def estimate(data,items,store):
    est = 0
    count = 0
    message = []
    data = data.loc[data["Store"] == store]

    for item, number in items.items():
        avg = data[data.loc[:, "Item"].str.contains(item)].loc[:, 'Per'].mean()
        if not math.isnan(avg):
            est += avg * number
        else:
            count += 1
            message.append(item)

    return [count, message, est]