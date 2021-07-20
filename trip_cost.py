import math

ls = [
        {"city" : "paris", "flight" : 200, "hotel" : 20, "car" : 200},
        {"city" : "london", "flight" : 250, "hotel" : 30, "car" : 120},
        {"city" : "dubai", "flight" : 370, "hotel" : 15,"car" : 80},
        {"city" : "mumbai", "flight" : 450,"hotel" : 10,"car" : 70}
]

def trip_cost(d,day):
    if day <= 7:
        week_ls = []
        for i in d:
            cost = i["flight"] + (i["hotel"]*day) + i["car"]
            i["total cost"] = cost
            week_ls.append(i)
        return (min(week_ls, key = lambda i : i.get("total cost")))
    
    
    elif day > 7:
        week_ls_3 = []
        for i in d:
            cost = i["flight"] + (i["hotel"]*day) + (i["car"]*(math.ceil(day/7)))
            i["total cost"] = cost
            week_ls_3.append(i)
        return (min(week_ls_3, key = lambda i : i.get("total cost")))
    
days = int(input("For how many days you are planning for your Trip: "))

week = math.ceil(days/7)
less_trip_cost = trip_cost(ls, days)
city = (less_trip_cost['city']).title()
flight = less_trip_cost['flight']
hotel =less_trip_cost['hotel']
car =less_trip_cost['car']
total = less_trip_cost['total cost']

print(f"\nMinimun Cost For your {days} days trip is $ {total} at {city}")
# print(f"\nFlight Ticket = $ {flight} \nHotel Rent for {days} days = $ {hotel} \nCar Rent for {week} week(s) = $ {car}")
print(f"\nFlight Ticket = $ {flight} \nHotel Rent per day = $ {hotel} \nCar Rent per week = $ {car}")
