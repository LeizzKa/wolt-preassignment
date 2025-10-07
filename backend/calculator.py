import datetime


def calculator(delivery_distance, item_amount, cart_value, year, month, day, hour, minute):
    #Declare variables we're going to use to calculate the fees

    surcharge: float = 0.0
    total_fees: float = 0.0
    delivery_fee: float = 0.0
    delivery_distance: float
    item_amount: float
    cart_value: float


    #Declare date and time separately to make friday rush check easier to read

    date = datetime.date(year, month, day)
    time = datetime.time(hour, minute)
    is_friday = date.weekday() == 4
    is_after15 = time >= datetime.time(15, 00)
    is_before19 = time >= datetime.time(19, 00)

    #Check the item amount and add bulk fee if needed 
    if item_amount >= 5:
        if item_amount > 12:
            surcharge += 1.2
        while item_amount > 4:
            surcharge += 0.5
            item_amount -=1  

    #Check delivery distance and calculate the delivery fee
    if delivery_distance < 1000:
        #If the user enters a negative delivery distance, we just return an error
        if delivery_distance < 0:
            return "Error: Please enter a valid distance"
        delivery_fee = 1
    elif delivery_distance == 1000:
        delivery_fee = 2
    else:
        #Set delivery fee to 2 for distances over 
        delivery_fee = 2
        extra_distance = delivery_distance - 1000
        while (extra_distance / 500) > 0:
           delivery_fee += 1
           extra_distance -= 500

    if cart_value < 10:
        surcharge = 10 - cart_value
    elif cart_value >= 100:
        surcharge = 0
        delivery_fee = 0
    else:
        pass

    
    total_fees = surcharge + delivery_fee
    

    if is_friday and (is_after15 or is_before19):
        total_fees = total_fees*1.2

    if total_fees > 15:
        total_fees = 15

    #Convert to cents and round to the nearest 1 cent
    total_fees_in_cents = total_fees * 100
    total_fees_in_cents = round(total_fees_in_cents, 1)

    return total_fees_in_cents

    if __name__ == "__main__":
        calculator(1000, 4, 10, 2023, 6, 21, 43)
