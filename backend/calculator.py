from units import unit
from valuta.shortcuts import display_in_currency_units
import datetime
import valuta

def calculator(delivery_distance, item_amount, cart_value):
    metres = unit('m')
    surcharge = 0
    total: float = 0
    delivery_fee: valuta
    max_fee: float = display_in_currency_units("EUR", 1_500)
    delivery_distance: float = metres
    item_amount: float
    cart_value: float = display_in_currency_units("EUR", 0)
    friday_rush: datetime
    
    
    if cart_value > display_in_currency_units("EUR", 1_000):
        surcharge = display_in_currency_units("EUR", 1_000) - cart_value
    else:
        pass
        
    if item_amount >= 5:
        extra_items = item_amount - 4
        for item in extra_items:
            surcharge = surcharge + display_in_currency_units("EUR", 50)
    else:
        pass

    if metres(delivery_distance) <= metres(1000):
        delivery_fee = display_in_currency_units("EUR", 200)
    else:
        extra_distance = metres(delivery_distance) - metres(1000)
        times_over_base = 0
        while metres(extra_distance) > metres(500):
            times_over_base+1
        for i in times_over_base:
            delivery_fee = delivery_fee + display_in_currency_units("EUR", 100)


    total_fees = cart_value + surcharge + delivery_fee
    if total_fees > display_in_currency_units("EUR", 1_500):
        total_fees = display_in_currency_units("EUR", 1_500)
    else:
        pass

    
    date = datetime.date()
    is_friday = date.weekday() == 4
    friday_rush = None

    print("Your surcharge is " + surcharge)
    print("Your delivery fees are " + delivery_fee)
    print("Your total is: " + total_fees)


if __name__ == "__main__":
    calculator(1000, 4, 10)
    #if is_friday and 15 <= date.hour() < 19 is True:

        