first_1000 = 7.633
beyond_1000 = 9.259

KW = int(input("Enter the KW hours used: "))
if KW <= 1000:
    cost = KW * first_1000
else:
    cost=(1000*first_1000) + ((KW - 1000) * beyond_1000)
cost=cost/100
print("Amount owed is $",cost)