def taxi_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare
def calculate_total_fare(trips):
    total_fare = 0
    for i in range(len(trips)):
        trip_fare = taxi_fare(trips[i])
        print(f"Trip {i + 1}: ${trip_fare:.2f}")
        total_fare += trip_fare
    return total_fare
trips = list(map(int,input("Enter trip distance in km: ").split()))
total_fare = calculate_total_fare(trips)
print(f"Total Fare: ${total_fare:.2f}")