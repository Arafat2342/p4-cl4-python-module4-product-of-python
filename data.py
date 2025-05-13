# given tuples

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

tuples1 = list(tup1)
tuples = list(tup2)

lst = []

print(tuples)
print(tuples1)

for tup in tuples:
    product = tup
    for mul in tuples1:
        product = tup * mul
lst.append(product)


print(f"\n{lst}\n")