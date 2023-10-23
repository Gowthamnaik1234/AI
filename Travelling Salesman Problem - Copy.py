from itertools import permutations

def calculate_total_distance(order, cities):
    total_distance = 0
    num_cities = len(order)

    for i in range(num_cities):
        from_city = cities[order[i]]
        to_city = cities[order[(i + 1) % num_cities]]
        total_distance += calculate_distance(from_city, to_city)

    return total_distance

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def traveling_salesman_bruteforce(cities):
    num_cities = len(cities)
    city_indices = list(range(num_cities))
    best_order = None
    best_distance = float('inf')

    for order in permutations(city_indices):
        distance = calculate_total_distance(order, cities)
        if distance < best_distance:
            best_distance = distance
            best_order = order

    return best_order, best_distance

if __name__ == "__main__":
    cities = [(0, 0), (2, 4), (3, 1), (4, 3)]  # Example cities represented as (x, y) coordinates

    best_order, best_distance = traveling_salesman_bruteforce(cities)

    print("Best order of cities:", best_order)
    print("Shortest distance:", best_distance)
