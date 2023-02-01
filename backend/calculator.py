import datetime
import decimal

def calculator(delivery_distance, item_amount, cart_value, year, month, day, hour, minute):
    surcharge: decimal = 0.0
    total_fees: decimal = 0.0
    delivery_fee: decimal = 0.0
    max_fee: decimal
    delivery_distance: decimal
    item_amount: decimal
    cart_value: decimal
    friday_rush: datetime

    date = datetime.date(year, month, day)
    time = datetime.time(hour, minute)
    is_friday = date.weekday() == 4
    is_after15 = time >= datetime.time(15, 00)
    is_before19 = time >= datetime.time(19, 00)
        
    if item_amount >= 5:
        if item_amount > 12:
            print("Bulk fee added")
            surcharge += 1.2
        while item_amount > 4:
            surcharge += 0.5
            item_amount -=1  
        else:
            pass
    else:    
        pass

    if 500 < delivery_distance <= 1000:
        delivery_fee = 2
    elif delivery_distance < 500:
        delivery_fee = 1
    else:
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

    if is_friday and is_after15 or is_before19:
        print("Friday rush bonus added")
        total_fees = total_fees*1.2
    else:
        pass

    if total_fees > 15:
        total_fees = 15
    else:
        pass
    total_fees = round(total_fees, 2)
    print("Your surcharge is:", surcharge, "€")
    print("Your delivery fees are:", delivery_fee, "€")
    print("Your total is:", total_fees, "€")

    return total_fees


if __name__ == "__main__":
    calculator(3000, 4, 80, 2023, 2, 3, 16, 40)

        