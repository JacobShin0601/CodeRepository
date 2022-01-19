price1 = float(input("Enter price of the first item: "))
price2 = float(input("Enter price of the second item: "))
card_YN = str(input("Does customer have a club card? (Y/N): "))
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))


card_YN = card_YN.lower()


base_price = price1 + price2



if(price1<price2):
    price_high = price2
    price_low = price1
else:
    price_high = price1
    price_low = price2

discounted_price = price_high + (0.5 * price_low)

if (card_YN == "y"):
    discounted_price = discounted_price * 0.9

total_price = discounted_price * (1 + tax_rate/100)

total_price = round(total_price, 2)


print("Base price = %2.2f" %base_price)
print("Price after discounts = %2.2f" %discounted_price)
print("Total price = %2.2f" %total_price)

#Enter tax rate, e.g. 5.5 for 5.5% tax: 8.25
#Base price = 30.00
#Price after discounts = 22.50
#Total price = 24.36