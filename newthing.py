
orders = ["Sandwiches:", "", "Fries?", "", "Drink Size:", "", "number of ketchup packets:", 0]

loop = True
while loop:
    sandwich_index = 1
    fries_index = 3
    drink_index = 5
    ketchup_index = 7

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

    fries = input("do you want fries? yes or no:")
    if fries == "yes":
        cost = cost + 1.50
        mega_size = input("do you want to mega-size? yes or no:")
        if mega_size == "yes":
            cost = cost + 1.00

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

    # Coupon code, where if they ordered everything, cost is reduced by 1.00
    if order in ["chicken", "beef", "tofu"] and fries == "yes" and drink in ["super-grande", "extra-small"] and packets > 0:
        cost = cost - 1.00
        print("yay, you get $1.00 off")
    print("final cost: $" + str(cost))

    # list code

    orders[sandwich_index] = orders[sandwich_index] + order
    orders[fries_index] = orders[fries_index] + fries 
    orders[drink_index] = orders[drink_index] + drink 
    orders[ketchup_index] = orders[ketchup_index] + packets
    print("your order:")
    print("(your ordered" + str(orders) + ")")
    continue_ordering = input("do you want to order again? yes or no:")
    if continue_ordering == "no":
        loop = False
        #code 
        print("your orders:")
        print(orders)
        print("total cost: $" + str(total_cost))
        print ("thank you for ordering, your final cost is: $" + str(cost))
    if continue_ordering == "yes":
        loop = True
    #code
    if continue_ordering == "yes":
        total_cost = 0
        total_items = 0
        total_cost = total_cost + cost
        total_items = total_items + 1
        print("total cost: $" + str(total_cost))
        print("total items ordered: " + str(total_items))