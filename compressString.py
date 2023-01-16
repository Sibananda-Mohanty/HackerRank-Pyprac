from itertools import groupby

string_of_numbers = input()

for key, items in groupby(string_of_numbers):
    items = list(items)
    print( tuple([len(items), int(key)]), end = ' ')