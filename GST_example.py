def calc_GST(init_price):
    GST_RATE = 0.15
    gst_amount = GST_RATE * init_price
    print("Initial price: ${:.2f}".format(init_price))
    print("GST added: ${:.2f}".format(gst_amount))
    print("Total cost: ${:.2f}".format(init_price + gst_amount))
    return init_price + gst_amount

prices = []

while True:
    price = float(input("Please enter price: "))
    thing = calc_GST(price)
    prices.append(thing)
    again = input("Type 'q' to quit, any other key to continue: ")
    if again == 'q':
        print("Ok, bye")
        break

print(prices)
