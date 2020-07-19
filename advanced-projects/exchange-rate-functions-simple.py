"""
WAP that converts exchange rate data

'convert' function:
- takes 2 values as parameters (initial value, rate)
- converts between any values which the user provides
- returns converted value

'get_info' function:
- gets user info
- calls 'convert' with user info as arguments
"""

def convert(start_val, rate):
    conv_val = start_val * rate
    return conv_val

def get_code(name):
    code = ""
    while len(code) != 3:
        code = input("Enter the 3 letter code for the {} currency: ".format(name))
        if len(code) != 3:
            print("Please enter exactly 3 characters")
    return code.upper()

def get_info():
    new_list = []
    amount = float(input("Enter initial currency value: "))
    curr1 = get_code("initial")
    curr2 = get_code("converted")
    rate = float(input("Enter conversion rate from {} to {}: ".format(curr1, curr2)))
    converted_amount = convert(amount, rate)
    print("{:.2f} {} is equivalent to {:.2f} {} at a rate of {}".format(amount, curr1, converted_amount, curr2, rate))
    new_list.append(amount)
    new_list.append(curr1)
    new_list.append(converted_amount)
    new_list.append(curr2)
    new_list.append(rate)

    for item in new_list:
        print(item)

get_info()

