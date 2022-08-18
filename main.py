import pandas as pd

female = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')
male = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')
names = pd.concat([female, male])
names = names.sort_values("nome").loc[:, "nome"].values.tolist()


def find(lists, target):
    start = 0
    end = len(lists) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = lists[middle]
        if midpoint == target:
            print(midpoint + " was found")
            return
        elif midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
    else:
        print(target + " was not found")
        return


name = input("Enter a name: ")
find(names, name.upper())
