dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

total_amount = dollars*100 + cents

quarters = total_amount//25
total_amount = total_amount - quarters*25
dimes = total_amount//10
total_amount = total_amount - dimes*10
nickels = total_amount//5
total_amount = total_amount - nickels*5
pennies = total_amount

print("The coins are", quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")
