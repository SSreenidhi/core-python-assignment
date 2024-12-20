"""7. Taxi Fare Calculation
Scenario:
A taxi service calculates fares based on the following rates: 
- **Base fare**: $50 
- **Distance fare**: $10/km 
Write a program to calculate the total fare for multiple trips.
Requirements:
- Use a function to calculate fare for each trip.
Input Example
```python
trips = [5, 10, 3]  # Distances in km
```
Expected Output:
```
Trip 1: $100
Trip 2: $150
Trip 3: $80
Total Fare: $330
"""

def calculate_fare(distance):
    return 50 + (10 * distance)

def calculate_total_fare(trips):
    fares = [calculate_fare(trip) for trip in trips]
    return fares, sum(fares)

trips = [5, 10, 3]
fares, total_fare = calculate_total_fare(trips)

for i, fare in enumerate(fares, 1):
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total_fare}")
