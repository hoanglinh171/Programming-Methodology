"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""

INPUT_FILE = 'bill2.txt'


def main():
    bill_dict = {}

    file = open(INPUT_FILE)
    for line in file:
        line = line.strip()
        location = find_location(line)
        price = find_price(line)
        if location in bill_dict:
            bill_dict[location] += price
        else:
            bill_dict[location] = price

    for key in bill_dict.keys():
        print(str(key) + ": " + "$" + str(bill_dict[key]))


def find_location(str):
    open_bracket = str.find("[")
    close_bracket = str.find("]")
    location = str[open_bracket + 1:close_bracket]
    return location


def find_price(str):
    dollar_sign = str.find("$")
    price = float(str[dollar_sign + 1:])
    return price


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
