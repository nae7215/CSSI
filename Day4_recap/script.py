# sales_tax = 0.09
#
# prices = {
#     'water':1.00,
#     'milk':1.50,
#     'apple':.75,}
#
# def calculate_tax(sale_value):
#     tax_value = sale_value * sales_tax
#     return tax_value
#
# calculate_tax(1)
#
# def calculate_final_price(sale_value):
#     final_price = sale_value + calculate_tax(sale_value)
#     return final_price
#
# def calculate_price_by_name(item_name):
#     final_price = calculate_final_price(prices[item_name])
#     if item_name in prices:
#         return final_price
#     else:
#         print ('No item found')
#
# print('Please insert item name')
# user_input = raw_input()
#
# print calculate_price_by_name(user_input)

answer1 = raw_input("What is the capital of Illinois?: ")

if answer1 == "Springfield":
    print "You are so smart!"
else
