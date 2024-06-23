"""
This program will calculate the total cost of a holiday
including rental car, flights and hotel costs
"""

"""get users inputs
    for city they are visiting,
    number of nights 
    days using the rental
create functions for
    hotel costs using the number of nights
    plane costs using the city they are visiting
    cost of car rental
    total cost of holiday
"""
# Dicts used to display pricing for end user
flight_cost = {"Rome": 120, "Berlin": 160, "New York": 220, "Madrid": 140}
city_hotel = {"Rome": 40, "Berlin": 45, "New York": 40, "Madrid": 50}

# Get input for city
print(flight_cost)
city_flight = input(str("Please Enter a city listed above: "))

# Get input for nights at hotel
print(city_hotel)
nights = input("How many nights are you planning to stay at the hotel?: ")
num_nights = int(nights)

# Get input for days with rental car
rental_days = input("How many days do you need to hire a car for?: ")
rental_num = int(rental_days)


# Function for getting the cost of hotel * per night fee
def hotel_cost(hotel):
    if city_flight == "Rome":
        hotel = num_nights * 40
    elif city_flight == "Berlin":
        hotel = num_nights * 45
    elif city_flight == "New York":
        hotel = num_nights * 40
    elif city_flight == "Madrid":
        hotel = num_nights * 50
    else:
        print("Invalid City")
    return int(hotel)


# Function for getting price of flight
def plane_cost(city):
    if city_flight == "Rome":
        city = 120
    elif city_flight == "Berlin":
        city = 160
    elif city_flight == "New York":
        city = 220
    elif city_flight == "Madrid":
        city = 140
    else:
        print("Invalid City")
    return int(city)


# Function for getting total cost of rental car days
def car_rental():
    car = rental_num * 30
    return int(car)


# Function for determining the total cost of holiday
# using hotel_cost(), plane_cost() and car_rental()
def holiday_cost():
    total_cost = hotel_cost(0) + plane_cost(0) + car_rental()
    return int(total_cost)


# Print statements for clean view of pricing
print(f"\nFlying to {city_flight} will cost: {plane_cost(0)}")
print(f"Price to stay at hotel for {num_nights} nights: {hotel_cost(0)}")
print(f"You have requested a rental car for {rental_num} days. This costs an additional: {car_rental()}")
print(f"The total cost for this holiday is {holiday_cost()}")


# This works but is outside of actual task


# def holiday_cost(total):
#     num_nights = int(nights)
#     rental_num = int(rental)
#     rental_days = 30 * rental_num
#     """if/else statement that checks city, adds the cost of hotel
#     per night with flight price and rental days for vehicle.
#     Throws an error if incorrect city entered"""
#     if city_flight == "Rome":
#         total = (40 * num_nights) + 120 + rental_days
#     elif city_flight == "New York":
#         total = (40 * num_nights) + 220 + rental_days
#     elif city_flight == "Berlin":
#         total = (45 * num_nights) + 160 + rental_days
#     elif city_flight == "Madrid":
#         total = (50 * num_nights) + 140 + rental_days
#     else:
#         print("Invalid City")
#     return total
#
#
# print(f"\nThe total cost of your trip to {city_flight} is {holiday_cost(0)}.")

