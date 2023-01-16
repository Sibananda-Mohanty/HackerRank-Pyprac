number_of_shoes = int(input())

from collections import Counter
shoes_avilability = Counter(input().split())

revnue = 0

number_of_customers = int(input())

for _ in range(number_of_customers):
    size, amount = input().split()
    if size in shoes_avilability.elements():
        revnue += int(amount)
        shoes_avilability.update({size: -1})
print(revnue)