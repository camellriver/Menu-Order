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

