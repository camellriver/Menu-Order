# sandwich code

print("sandwiches: chicken $2.95, beef $9.99, tofu $1.00")
order = input("what you want:")
if order == "chicken":
    cost = 2.95
    print("ok, chicken")
elif order == "beef":
    cost = 9.99
    print("ok, you like beef")
elif order == "tofu":
    cost = 1.00
    print("ok, you like tofu")
else:
    print("we aint got that")

# fries code

fries = input("yes or no:")
if fries == "yes":
    cost = cost + 1.50
print("current cost: $" + str(cost))

# drink code

print("drinks: super-grande $1.50, extra-small $1.00")
drink = input("what drink you want:")
if drink == "super-grande":
    cost = cost + 1.50
elif drink == "extra-small":
    cost = cost + 1.00
else:
    print("we dont got that")
print("current cost: $" + str(cost))

# ketchup packets code

print("want ketchup packets? $0.25 each")
packets = float(input("how many you want:"))
packetcost = (packets * .25)
cost = cost + packetcost
print("current cost: $" + str(cost))